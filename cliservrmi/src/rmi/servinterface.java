package rmi;

import java.rmi.*;
import java.rmi.server.ServerNotActiveException;


public interface servinterface extends Remote {
    public double inter (double a) throws RemoteException,ServerNotActiveException;
    public double min (double a,String c) throws RemoteException,ServerNotActiveException;
    public double game (double a,String c) throws RemoteException,ServerNotActiveException;
}
