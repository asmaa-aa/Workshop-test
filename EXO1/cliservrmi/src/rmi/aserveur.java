package rmi;

//import com.sun.org.apache.xml.internal.utils.StopParseException;
import java.rmi.Naming;
import java.rmi.RemoteException;
import java.rmi.registry.LocateRegistry;
import java.rmi.server.ServerNotActiveException;
import java.rmi.server.UnicastRemoteObject;
import javax.swing.JFrame;
import java.math.*;
import javax.swing.JOptionPane;
//import sun.java2d.Disposer;

public class aserveur extends UnicastRemoteObject implements servinterface {

    public aserveur() throws RemoteException{
    }

    
    public void exe (String d){
        try{
            servinterface abc = new aserveur();
            LocateRegistry.createRegistry(Integer.parseInt(d));
            Naming.rebind("rmi://127.0.0.1:"+d+"/servinterface", abc);
            System.out.println("server is ready .");
        
        }catch(Exception e){
            System.out.println(" server failed:"+e);
            JOptionPane.showMessageDialog(new JFrame(), "LE SERVEUR N'EST PAS CONNECTER");
        }
    }

    
    

    @Override
    public double inter(double a) throws RemoteException, ServerNotActiveException {
        double result = 0;
        
        try {
        result = a;
        Serv.it.add(result);
        System.out.println("sise00 :"+Serv.it.size());
        
        }catch(Exception e){
        }
        return result;
    }

    @Override
    public double min(double a,String c) throws RemoteException, ServerNotActiveException {
        double result = 0;
        
        try {
            result = a;
            Serv.it.add(result);
            System.out.println("sise00 :"+Serv.it.size());
        }
        catch(Exception e){
        }
        
        double min =100000;
        
        try {
            System.out.println("sise :"+Serv.it.size());
            
            for (int i = 0; i < Serv.it.size(); i++) {
                double m= Double.parseDouble(Serv.it.get(i).toString());
                min=Math.min(m,min);
            }
        }catch(Exception e){
        }
        
        return min;
    }

    @Override
    public double game(double a, String c) throws RemoteException, ServerNotActiveException {
        
        double result = 0;
        double choix = 0;
        
        try {
            choix = a;
            Serv.it.add(choix);
            System.out.println("sise00 :"+Serv.it.size());
        }
        catch(Exception e){
        }
        
        try {
            System.out.println("sise :"+Serv.it.size());
            
            for (int i = 0; i < Serv.it.size(); i++) {
        
                double ch= Double.parseDouble(Serv.it.get(i).toString());
        
                if(choix == ch)
                    result = 0;
                
                if(choix==1 && ch==3)
                    result = 1;
        
                if(choix==2 && ch==1)
                    result = 1;
        
                if(choix==3 && ch==2)
                    result = 1;
        
                if(choix==1 && ch==2)
                    result = 2;
        
                if(choix==2 && ch==3)
                    result = 2;
        
                if(choix==3 && ch==1)
                    result = 2;
            }
        }catch(Exception e){
        }
        return result;

    }    
}
        