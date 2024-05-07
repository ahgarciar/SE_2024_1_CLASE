const express = require('express')

const controller = require('../../controllers/ControllerSistemasEmbebidos')

//RUTAS
const router = express.Router()

// /api/v1/
router
   // http://localhost:3000/api/v1/
  .get("/", controller.getAll_Historico_Dispositivos)  //RETORNA TODO EL HISTORICO
  
  // http://localhost:3000/api/v1/###
  .get("/:idDispositivo", controller.getDispositivo_Historico)

  // http://localhost:3000/api/v1/dispositivos/###
  .get("/dispositivos/:idDispositivo", controller.getLastDispositivoHistorico) 
  
  //INSERT NEW HISTORICO
  // http://localhost:3000/api/v1/
  .post("/", controller.insertHistorico) 

  //UPDATE HISTORICO
  // http://localhost:3000/api/v1/
  .put("/:idHistorico", controller.updateHistorico) 
  
  //DELETE HISTORICO
  // http://localhost:3000/api/v1/
  .delete("/", controller.deleteHistorico) 

  //EXPORTA EL ROUTER PARA HACER POSIBLE SU POSTERIOR IMPORTANCION Y USO EN OTROS MODULOS
module.exports = router;