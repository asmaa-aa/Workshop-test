/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */

package rmi;
import java.net.MalformedURLException;
import java.rmi.Naming;
import java.rmi.NotBoundException;
import java.rmi.RemoteException;
import java.rmi.server.ServerNotActiveException; 


public class client {
    
    
    
    
    public double exe_cli_game (String c,String u,String ee) throws NotBoundException, MalformedURLException, RemoteException, ServerNotActiveException{
        
        double v = 0 ;
        servinterface lp=(servinterface) Naming.lookup("rmi://"+u+":"+ee+"/servinterface");
        
        v = lp.game(c);
        
        return v;
    }
    
    
    public double exe_cli_choice (double score ,double a,String c,String u,String ee) throws NotBoundException, RemoteException, ServerNotActiveException, MalformedURLException{
        
        double v = 0 ;
        servinterface lp=(servinterface) Naming.lookup("rmi://"+u+":"+ee+"/servinterface");
        
        v = lp.choice(score,a,c);
        
        return v; 
    }
     public double exe_cli_choice2(String c,String u,String ee) throws NotBoundException, RemoteException, ServerNotActiveException, MalformedURLException{
        
        double v = 0 ;
        servinterface lp=(servinterface) Naming.lookup("rmi://"+u+":"+ee+"/servinterface");
        
        v = lp.choice2(c);
        
        return v; 
    }
    
    

    public static void main(String[] argv) {
    }

}
