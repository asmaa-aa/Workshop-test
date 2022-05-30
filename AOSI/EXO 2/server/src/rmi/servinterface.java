/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */

package rmi;

import java.rmi.*;
import java.rmi.server.ServerNotActiveException;

/**
 *
 * @author PC
 */

public interface servinterface extends Remote {
public double inter (double a) throws RemoteException,ServerNotActiveException;
public double min (double a,String c) throws RemoteException,ServerNotActiveException;
}
