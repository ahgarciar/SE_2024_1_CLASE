-- EJECUTAR PASO POR PASO Y NO AL SCRIPT COMPLETO DE UNA VEZ...

--PASO 1 -- CREACION DE LA BASE DE DATOS 
USE MASTER
GO
CREATE DATABASE [BD_API_SISTEMAS_EMBEBIDOS]

--PASO 2 SELECCION DE LA BASE DE DATOS PARA APLICAR CAMBIOS SOBRE ELLA 
USE BD_API_SISTEMAS_EMBEBIDOS
GO

--PASO 3 CREACION DE TABLA TIPO_DISPOSITIVO
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Tipo_Dispositivo](
	[id_tipo] [int] IDENTITY(1,1) NOT NULL,
	[nombre_tipo] [varchar](255) NULL,	
) ON [PRIMARY]
GO
ALTER TABLE [dbo].[Tipo_Dispositivo] ADD PRIMARY KEY CLUSTERED 
(
	[id_tipo] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, IGNORE_DUP_KEY = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
GO


--PASO 4 CREACION DE TABLA DISPOSITIVOS
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Dispositivos](
	[id_dispositivo] [int] IDENTITY(1,1) NOT NULL,
	[nombre_dispositivo] [varchar](255) NULL,
	[id_tipo] [int] NULL
) ON [PRIMARY]
GO
ALTER TABLE [dbo].[Dispositivos] ADD PRIMARY KEY CLUSTERED 
(
	[id_dispositivo] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, IGNORE_DUP_KEY = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
GO


--PASO 5 CREACION DE TABLA HISTORICO
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Historico](
	[id_historico] [int] IDENTITY(1,1) NOT NULL,
	[id_dispositivo] int,	
    [fecha] [datetime] NULL,	
    [valor] [int],	
) ON [PRIMARY]
GO
ALTER TABLE [dbo].[Historico] ADD PRIMARY KEY CLUSTERED 
(
	[id_historico] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, IGNORE_DUP_KEY = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
GO


--- PROCEDIMIENTOS ALMACENADOS

--PASO 6
ALTER PROCEDURE [dbo].[SP_Insert_Tipo_Dispositivo] 
    -- Add the parameters for the stored procedure here    
	@nombre_tipo as varchar(255)	
AS
BEGIN
    -- SET NOCOUNT ON added to prevent extra result sets from
    -- interfering with SELECT statements.
    SET NOCOUNT ON;

    INSERT INTO [dbo].[Tipo_Dispositivo]
           (
	        [nombre_tipo]            
           )
     VALUES
           (
            @nombre_tipo
           )
    
END


---PASO 7
exec SP_Insert_Tipo_Dispositivo 'Analogico'
exec SP_Insert_Tipo_Dispositivo 'Digital'
exec SP_Insert_Tipo_Dispositivo 'HIBRIDO'

select * from Tipo_Dispositivo
GO


--PASO 8

CREATE PROCEDURE [dbo].[SP_Insert_Dispositivos] 
    -- Add the parameters for the stored procedure here    
	@nombre_dispositivo as varchar(255),
	@id_tipo as int	
AS
BEGIN
    -- SET NOCOUNT ON added to prevent extra result sets from
    -- interfering with SELECT statements.
    SET NOCOUNT ON;

    INSERT INTO [dbo].[Dispositivos]
           (
	        [nombre_dispositivo],
            [id_tipo]            
           )
     VALUES
           (
            @nombre_dispositivo,
            @id_tipo            
           )
    
END


---PASO 9
exec SP_Insert_Dispositivos "LED", 2
exec SP_Insert_Dispositivos "POTENCIOMETRO", 1

select * from Dispositivos
GO


--PASO 10
CREATE PROCEDURE [dbo].[SP_Insert_Historico] 
    -- Add the parameters for the stored procedure here    
	@id_dispositivo as int,
	@valor as int
AS
BEGIN
    -- SET NOCOUNT ON added to prevent extra result sets from
    -- interfering with SELECT statements.
    SET NOCOUNT ON;

    INSERT INTO [dbo].[Historico]
           (
	        [id_dispositivo],
            [valor],
            [fecha]            
           )
     VALUES
           (
            @id_dispositivo,
            @valor,
            GETDATE()
           )
    
END


---PASO 11
exec SP_Insert_Historico 1, 1
exec SP_Insert_Historico 2, 400
exec SP_Insert_Historico 2, 600

select * from Historico
GO

--PASO 12
CREATE PROCEDURE [dbo].[SP_Update_Historico] 
    -- Add the parameters for the stored procedure here    
	@id_historico as int,
    @valor as int	
AS
BEGIN
    -- SET NOCOUNT ON added to prevent extra result sets from
    -- interfering with SELECT statements.
    SET NOCOUNT ON;

    UPDATE [dbo].[Historico]
    SET valor = @valor
    WHERE 
    id_historico = @id_historico
    
END

---PASO 13
exec SP_Update_Historico 2,  300 

select * from Historico

GO

---PASO 14
CREATE PROCEDURE [dbo].[SP_Delete_Historico] 
    -- Add the parameters for the stored procedure here    
	@id_historico as int	
AS
BEGIN
    -- SET NOCOUNT ON added to prevent extra result sets from
    -- interfering with SELECT statements.
    SET NOCOUNT ON;

    DELETE FROM [dbo].[Historico]
    WHERE 
    id_historico = @id_historico
    
END

---PASO 15

exec SP_Delete_Historico 2

select * from Historico

GO


---PASO 16 
CREATE PROCEDURE [dbo].[SP_SelectALL_Dispositivos_Historico]
    -- Add the parameters for the stored procedure here 
AS
BEGIN
    -- SET NOCOUNT ON added to prevent extra result sets from
    -- interfering with SELECT statements.
    SET NOCOUNT ON;

    SELECT id_historico, nombre_dispositivo, nombre_tipo, valor, fecha FROM Historico 
    INNER JOIN Dispositivos ON Historico.id_dispositivo = Dispositivos.id_dispositivo
    INNER JOIN Tipo_Dispositivo ON Tipo_Dispositivo.id_tipo =  Dispositivos.id_tipo
    ORDER BY fecha DESC

END

select * from Dispositivos
INSERT INTO Dispositivos (nombre_dispositivo, id_tipo) VALUES('LDR', 1)

--PASO 17
EXEC SP_SelectALL_Dispositivos_Historico
GO

---PASO 18
CREATE PROCEDURE [dbo].[SP_Select_Dispositivo_Historico]
    -- Add the parameters for the stored procedure here 
    @id_dispositivo as int
AS
BEGIN
    -- SET NOCOUNT ON added to prevent extra result sets from
    -- interfering with SELECT statements.
    SET NOCOUNT ON;

    SELECT id_historico, nombre_dispositivo, nombre_tipo, valor, fecha FROM Historico 
    INNER JOIN Dispositivos ON Historico.id_dispositivo = Dispositivos.id_dispositivo
    INNER JOIN Tipo_Dispositivo ON Tipo_Dispositivo.id_tipo =  Dispositivos.id_tipo
    where Historico.id_dispositivo = @id_dispositivo
    ORDER BY fecha DESC

END

--PASO 19
EXEC SP_Select_Dispositivo_Historico 2
GO

---PASO 20
CREATE PROCEDURE [dbo].[SP_SelectLastValor_Dispositivo_Historico]
    -- Add the parameters for the stored procedure here 
    @id_dispositivo as int
AS
BEGIN
    -- SET NOCOUNT ON added to prevent extra result sets from
    -- interfering with SELECT statements.
    SET NOCOUNT ON;

    SELECT TOP 1 id_historico, nombre_dispositivo, nombre_tipo, valor, fecha FROM Historico 
    INNER JOIN Dispositivos ON Historico.id_dispositivo = Dispositivos.id_dispositivo
    INNER JOIN Tipo_Dispositivo ON Tipo_Dispositivo.id_tipo =  Dispositivos.id_tipo
    where Historico.id_dispositivo = @id_dispositivo
    ORDER BY fecha DESC

END

--PASO 21
EXEC SP_SelectLastValor_Dispositivo_Historico 2
GO