import { combineReducers } from 'redux';
import auth from '../auth/auth';

const rootReducer = combineReducers({
  auth,
});

export default rootReducer;