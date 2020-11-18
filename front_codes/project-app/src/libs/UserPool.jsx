import { CognitoUserPool } from 'amazon-cognito-identity-js';

  // Cognito API
const poolData = {
    UserPoolId: 'ap-northeast-2_LUC2PVCHb',
    ClientId: '2kjcmq2gtfqdonn6qt4msbsfs4',
};
  
export default new CognitoUserPool(poolData);