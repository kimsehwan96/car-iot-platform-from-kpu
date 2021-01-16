import { AuthState, AuthAction, SET_LOADING, SET_USER, SIGN_OUT, SET_ERROR, SET_SUCCESS, NEED_VERIFICATION } from '../types';

const initialState: AuthState = {
  user: null,
  authenticated: false,
  loading: false,
  error: '',
  needVerification: false,
  success: '',
}

// eslint-disable-next-line import/no-anonymous-default-export
export default (state = initialState, action: AuthAction) => {
  switch(action.type) {
    case SET_USER:
      return {
        ...state,
        user: action.payload,
        authenticated: true,
      }
    case SET_LOADING:
      return {
        ...state,
        loading: action.payload,
      }
    case SIGN_OUT:
      return {
        ...state,
        user: null,
        authenticated: false,
        loading: false,
      }
     case SET_ERROR:
       return {
         ...state,
         error: action.payload,
       }
      case SET_SUCCESS:
        return {
          ...state,
          success: action.payload,
        }
      case NEED_VERIFICATION:
        return {
          ...state,
          needVerification: true,
        }
      default:
        return state;
  }
}