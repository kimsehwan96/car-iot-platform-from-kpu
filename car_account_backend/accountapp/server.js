const app = require('./app');
const dotenv = require('dotenv');

dotenv.config();

app.listen(process.env.DEVELOPMENT_PORT, () => {
  console.log('server start');
});