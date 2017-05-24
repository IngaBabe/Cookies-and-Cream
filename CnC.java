import java.io.*;
import java.net.*;
import java.util.*;
import javax.swing.JOptionPane;

public class CnC {
    public static void main(String[] args) throws Exception {
        Server myServer = new Server();
        Client myClient = new Client();
		myServer.start();
		JOptionPane.showMessageDialog(null,"Click ok to start the server" );
		myClient.start();
    }  
}
