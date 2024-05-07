const bd = require("../models/StoredProcedures")

/////////////////////////////////////////////////////////////////////////////////////////////////////////

const getAll_Historico_Dispositivos = async function(){    
    //return " Hola!!!!"
    const resp = await bd.SP_SelectALL_Dispositivos_Historico()
    //console.log("resp from service->", resp)
    return resp
}

/////////////////////////////////////////////////////////////////////////////////////////////////////////

const getDispositivo_Historico = async function(id){
    const resp = await bd.SP_Select_Dispositivo_Historico(id)
    //console.log("resp from service->", resp)
    return resp
}

/////////////////////////////////////////////////////////////////////////////////////////////////////////

const getLastDispositivoHistorico = async function(id){
    const resp = await bd.SP_SelectLastValor_Dispositivo_Historico(id)
    //console.log("resp from service->", resp)
    return resp
}

/////////////////////////////////////////////////////////////////////////////////////////////////////////

const insertHistorico = async function(JsonObj){
    console.log("Res: ", JsonObj) //CONFIRMACION DE DATOS RECIBIDOS
    
    id_dispositivo = JsonObj.Id_Dispositivo
    valor = JsonObj.Valor
    
    const resp = await bd.SP_Insert_Historico(id_dispositivo, valor)
    return resp
}

/////////////////////////////////////////////////////////////////////////////////////////////////////////

const updateHistorico = async function(id_historico, JsonObj){
    //console.log("Res: ", JsonObj) //CONFIRMACION DE DATOS RECIBIDOS

    valor = JsonObj.Valor
   
    const resp = await bd.SP_Update_Historico(id_historico, valor)
    return resp
}

/////////////////////////////////////////////////////////////////////////////////////////////////////////

const deleteHistorico = async function(JsonObj){
    console.log("Res: ", JsonObj) //CONFIRMACION DE DATOS RECIBIDOS

    id_historico = JsonObj.Id_Historico
    
    const resp = await bd.SP_Delete_Historico(id_historico)
    return resp
}

/////////////////////////////////////////////////////////////////////////////////////////////////////////

module.exports = {
    getAll_Historico_Dispositivos,
    getDispositivo_Historico,
    getLastDispositivoHistorico,
    
    insertHistorico,
    updateHistorico,
    deleteHistorico
   
}

