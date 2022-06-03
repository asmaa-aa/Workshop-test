package rmi;

import java.rmi.*;
import java.rmi.server.ServerNotActiveException;

public interface servinterface extends Remote {
   // public double inter (double a) throws RemoteException,ServerNotActiveException;
    public double game (String c) throws RemoteException,ServerNotActiveException;
    public double choice(double score,double a,String c) throws RemoteException,ServerNotActiveException;
    public double choice2(String c)throws RemoteException,ServerNotActiveException;
}
