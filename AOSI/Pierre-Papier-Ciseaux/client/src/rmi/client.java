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

    public double exe_cli_game(double number, String c, String u, String ee)
            throws NotBoundException, MalformedURLException, RemoteException, ServerNotActiveException {

        double v = 0;
        servinterface lp = (servinterface) Naming.lookup("rmi://" + u + ":" + ee + "/servinterface");

        v = lp.game(number, c);

        return v;
    }

    public double exe_cli_choice1(double number, double a, String c, String u, String ee)
            throws NotBoundException, RemoteException, ServerNotActiveException, MalformedURLException {

        double v = 0;
        servinterface lp = (servinterface) Naming.lookup("rmi://" + u + ":" + ee + "/servinterface");

        v = lp.choice1(number, a, c);

        return v;
    }

    public double exe_cli_choice12(double number, String c, String u, String ee)
            throws NotBoundException, RemoteException, ServerNotActiveException, MalformedURLException {

        double v = 0;
        servinterface lp = (servinterface) Naming.lookup("rmi://" + u + ":" + ee + "/servinterface");

        v = lp.choice12(number, c);

        return v;
    }

    public double exe_cli_choice2(double number, double a, String c, String u, String ee)
            throws NotBoundException, RemoteException, ServerNotActiveException, MalformedURLException {

        double v = 0;
        servinterface lp = (servinterface) Naming.lookup("rmi://" + u + ":" + ee + "/servinterface");

        v = lp.choice2(number, a, c);

        return v;
    }

    public double exe_cli_choice22(double number, String c, String u, String ee)
            throws NotBoundException, RemoteException, ServerNotActiveException, MalformedURLException {

        double v = 0;
        servinterface lp = (servinterface) Naming.lookup("rmi://" + u + ":" + ee + "/servinterface");

        v = lp.choice22(number, c);

        return v;
    }

    public static void main(String[] argv) {
    }

}
