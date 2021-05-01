const express = require('express');
const router = express.Router();
const swaggerJsdoc = require('swagger-jsdoc');
const swaggerUi = require('swagger-ui-express');

const options = {
  swaggerDefinition: {
    openapi: '3.0.0',
    info: {
      title: 'api-doc',
      version: '0.0.1',
      description: 'API Swagger Doc',
    },
    servers: [
      {
        url: 'http://localhost:3000',
        basePath: '/',
      },
    ],
  },
  apis: ['./routes/*.js'],
};

const specs = swaggerJsdoc(options);

router.use('/api-docs', swaggerUi.serve);
router.get(
  '/api-docs',
  swaggerUi.setup(specs, {
    explorer: true,
  })
);

module.exports = router;