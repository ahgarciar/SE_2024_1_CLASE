const {getConnection} = require('./Conexion')
const sql = require('mssql')

/////////////////////////////////////////////////////////////////////////////////////////////////////////
//RETORNA LOS REGISTROS HISTORICOS DE TODOS LOS DISPOSITIVOS
const SP_SelectALL_Dispositivos_Historico  = async function(){    
    const conexion = await getConnection()
    const result = await conexion
            .request().execute('SP_SelectALL_Dispositivos_Historico')
    //console.log(result.recordset)
    return result.recordset
}
/////////////////////////////////////////////////////////////////////////////////////////////////////////
//RETORNA TODOS LOS REGISTROS HISTORICOS DE UN DISPOSITIVO
const SP_Select_Dispositivo_Historico = async function(id_dispositivo){    
    const conexion = await getConnection()
    const result = await conexion
    .request()                      
         .input("id_dispositivo", sql.Int, id_dispositivo )        
         .execute('SP_Select_Dispositivo_Historico')
    //console.log(result.recordset)
    return result.recordset
}
/////////////////////////////////////////////////////////////////////////////////////////////////////////
//RETORNA AL ULTIMO REGISTRO HISTORICO DE UN DISPOSITIVOS
const SP_SelectLastValor_Dispositivo_Historico = async function(id_dispositivo){    
    const conexion = await getConnection()
    const result = await conexion
    .request()
        .input("id_dispositivo", sql.Int, id_dispositivo )
        .execute('SP_SelectLastValor_Dispositivo_Historico')
    //console.log(result.recordset)
    return result.recordset[0]
   //return "{\"Resultado\": \"Inserción Correcta\"}"
}
/////////////////////////////////////////////////////////////////////////////////////////////////////////
const SP_Insert_Historico = async function(id_dispositivo, valor){
    console.log("id_dispositivo: ", id_dispositivo, " valor:", valor) //CONFIRMACION DE VALORES RECIBIDOS
    const conexion = await getConnection()
    const result = await conexion
    .request()                   
         .input("id_dispositivo", sql.VarChar, id_dispositivo  ) //EL CASTEO A INT SE REALIZA IMPLICITO
         .input("valor", sql.Int, valor  )                              
         .execute('SP_Insert_Historico')
    //console.log(result)
    return "{\"Resultado\": \"Inserción Correcta\"}" //RETORNA UN OBJETO JSON
}
/////////////////////////////////////////////////////////////////////////////////////////////////////////
const SP_Update_Historico = async function(id_historico, valor){

    console.log("id_historico: ", id_historico, " valor:", valor) //CONFIRMACION DE VALORES RECIBIDOS

    const conexion = await getConnection()
    const result = await conexion
    .request()                         
         .input("id_historico", sql.Int, id_historico  )        
         .input("valor", sql.Int, valor  )              
         .execute('SP_Update_Historico')
    //console.log(result)
    return "{\"Resultado\": \"Actualizacion Correcta\"}" //RETORNA UN OBJETO JSON
}
/////////////////////////////////////////////////////////////////////////////////////////////////////////
const SP_Delete_Historico = async function(id_historico){

    console.log("id_historico: ", id_historico) //CONFIRMACION DE VALORES RECIBIDOS

    const conexion = await getConnection()
    const result = await conexion
    .request()                         
         .input("id_historico", sql.Int, id_historico  )            
         .execute('SP_Delete_Historico')
    //console.log(result)
    return "{\"Resultado\": \"Eliminación Correcta\"}" //RETORNA UN OBJETO JSON
}
/////////////////////////////////////////////////////////////////////////////////////////////////////////
///////////////////////////////////////////////////////////////////////////////////////////////////
//EXPORTA LAS FUNCIONES PARA HACER POSIBLE SU POSTERIOR IMPORTANCION Y USO EN OTROS MODULOS
module.exports = {
    SP_SelectALL_Dispositivos_Historico, 
    SP_Select_Dispositivo_Historico,
    SP_SelectLastValor_Dispositivo_Historico,  

    SP_Insert_Historico,
    SP_Update_Historico,
    SP_Delete_Historico,  
    
}
