import { ThunkAction } from "redux-thunk";
import { RootState } from "..";
import { AuthAction, NEED_VERIFICATION, SET_ERROR, SET_LOADING, SET_USER, SignInData, SignUpData, SIGN_OUT, User } from "../types";
import firebase from '../../firebase/config';

// Create User
export const signup = (data: SignUpData, onError: () => void): ThunkAction<void, RootState, null, AuthAction> => {
  return async dispatch => {
    try {
      const res = await firebase.auth().createUserWithEmailAndPassword(data.email, data.password);
      if(res.user) {
        const userData: User = {
          email: data.email,
          firstName: data.firstName,
          id: res.user.uid,
          createAt: firebase.firestore.FieldValue.serverTimestamp(),
        };
        await firebase.firestore().collection('/users').doc(res.user.uid).set(userData);
        await res.user.sendEmailVerification();
        dispatch({
          type: NEED_VERIFICATION
        });
        dispatch({
          type: SET_USER,
          payload: userData,
        });
      }
    } catch (error) {
      console.log(error);
      onError();
      dispatch({
        type: SET_ERROR,
        payload: error.message
      });
    }
  }
}

// Get User by Id
export const getUserById = (id: string): ThunkAction<void, RootState, null, AuthAction> => {
  return async dispatch => {
    try {
      const user = await firebase.firestore().collection('users').doc(id).get();
      if(user.exists) {
        const userData = user.data() as User;
        dispatch({
          type: SET_USER,
          payload: userData
        });
      }
    } catch (error) {
      console.log(error);
    }
  }
}

// Set Loading
export const setLoading = (value: boolean): ThunkAction<void, RootState, null, AuthAction> => {
  return dispatch => {
    dispatch({
      type: SET_LOADING,
      payload: value,
    });
  }
}

// Log in
export const signin = (data: SignInData, onError: () => void): ThunkAction<void, RootState, null, AuthAction> => {
  return async dispatch => {
    try {
      await firebase.auth().signInWithEmailAndPassword(data.email, data.password);
    } catch (error) {
      console.log(error);
      onError();
      dispatch(setError(error.message));
    }
  }
}

// Log out
export const signout = (): ThunkAction<void, RootState, null, AuthAction> => {
  return async dispatch => {
    try {
      dispatch(setLoading(true));
      await firebase.auth().signOut(); 
      dispatch({
        type: SIGN_OUT
      });
    } catch (error) {
      console.log(error);
      dispatch(setLoading(false));
    }
  }
}

// Set Error
export const setError = (msg: string): ThunkAction<void, RootState, null, AuthAction> => {
  return dispatch => {
    dispatch({
      type: 'SET_ERROR',
      payload: msg,
    });
  }
}

// Set need verification
export const setNeedVerification = ():  ThunkAction<void, RootState, null, AuthAction> => {
  return dispatch => {
    dispatch({
      type: NEED_VERIFICATION,
    });
  }
}

// Set Success
export const setSuccess = (msg: string): ThunkAction<void, RootState, null, AuthAction> => {
  return dispatch => {
    dispatch({
      type: 'SET_SUCCESS',
      payload: msg,
    });
  }
}

// Send password reset email
export const sendPasswordResetEmail = (email: string, successMsg: string): ThunkAction<void, RootState, null, AuthAction> => {
  return async dispatch => {
    try {
      await firebase.auth().sendPasswordResetEmail(email);
      dispatch(setSuccess(successMsg));
    } catch (error) {
      console.log(error);
      dispatch(setError(error.message));
    }
  }
}