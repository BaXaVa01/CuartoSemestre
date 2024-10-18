package com.uam;

import java.sql.*;



public class Conexion {

    private final String url = "jdbc:postgresql://localhost:5432/LibroDB";
    private final String user = "postgres";
    private final String password = "1822";



    public Connection connect() {

        Connection conex = null;


         try {
             conex=DriverManager.getConnection(url,user,password);
             System.out.println("Conectado exitosamente ");




         }catch (SQLException e) {
             System.out.println(e.getMessage());
         }
        return conex;
    }


    }




