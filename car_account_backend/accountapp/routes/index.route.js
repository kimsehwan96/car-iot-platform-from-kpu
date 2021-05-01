const express = require('express');
const router = express.Router();
const mainPage = require('../controllers/index.controller');

router.get('/', mainPage);

module.exports = router;