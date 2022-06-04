package rmi;

import java.rmi.*;
import java.rmi.server.ServerNotActiveException;


public interface servinterface extends Remote {
   // public double inter (double a) throws RemoteException,ServerNotActiveException;
    public double game (double number,String c) throws RemoteException,ServerNotActiveException;
    public double choice1(double number,double a,String c) throws RemoteException,ServerNotActiveException;
    public double choice2(double number,double a,String c) throws RemoteException,ServerNotActiveException;
    public double choice12(double number,String c)throws RemoteException,ServerNotActiveException;
    public double choice22(double number,String c)throws RemoteException,ServerNotActiveException;
}
