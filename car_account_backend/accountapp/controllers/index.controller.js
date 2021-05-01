const path = require('path');

const mainPage = (req, res) => {
  res.sendFile(path.resolve(__dirname, '..', 'index.html'));
};

module.exports = mainPage;