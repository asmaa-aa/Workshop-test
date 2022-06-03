package rmi;

//import com.sun.org.apache.xml.internal.utils.StopParseException;
import java.rmi.Naming;
import java.rmi.RemoteException;
import java.rmi.registry.LocateRegistry;
import java.rmi.server.ServerNotActiveException;
import java.rmi.server.UnicastRemoteObject;
import javax.swing.JFrame;
import javax.swing.JOptionPane;
//import sun.java2d.Disposer;

public class aserveur extends UnicastRemoteObject implements servinterface {
    double scoree;
    double choice2;

    public aserveur() throws RemoteException {
    }

    public void exe(String d) {
        try {
            servinterface abc = new aserveur();
            LocateRegistry.createRegistry(Integer.parseInt(d));
            Naming.rebind("rmi://127.0.0.1:" + d + "/servinterface", abc);
            System.out.println("server is ready .");

        } catch (Exception e) {
            System.out.println(" server failed:" + e);
            JOptionPane.showMessageDialog(new JFrame(), "LE SERVEUR N'EST PAS CONNECTER");
        }
    }

    public double game(String c) throws RemoteException, ServerNotActiveException {

        double result = 0;

        try {
            System.out.println("sise :" + Serv.it.size());

            for (int i = 0; i < Serv.it.size(); i++) {

                double ch = Double.parseDouble(Serv.it.get(i).toString());
                System.out.println("choix1    " + ch);
                double chh = Double.parseDouble(Serv.it.get(i + 1).toString());
                System.out.println("choix2     " + chh);

                choice2 = chh;
                if (ch == chh) {
                    result = 0;
                }

                if (ch == 1 && chh == 3) {
                    result = 1;
                }

                if (ch == 2 && chh == 1) {
                    result = 1;
                }

                if (ch == 3 && chh == 2) {
                    result = 1;

                }

                if (ch == 1 && chh == 2) {
                    result = 2;

                }

                if (ch == 2 && chh == 3) {
                    result = 2;
                }

                if (ch == 3 && chh == 1) {
                    result = 2;
                }

            }
        } catch (Exception e) {
        }
        return result;

    }

    @Override
    public double choice2(String c) throws RemoteException, ServerNotActiveException {

        double choic2 = 0 ;
        choic2 = choic2 +0;

        try {
            for (int i = 0; i < Serv.it.size(); i++) {
                choic2 = Double.parseDouble(Serv.it.get(i + 1).toString());
            }
        } catch (Exception e) {
        }

        return choice2;
    }

    @Override
    public double choice(double score, double a, String c) throws RemoteException, ServerNotActiveException {
        scoree = score;
        double choix = 0;

        try {

            choix = a;
            Serv.it.add(choix);
            System.out.println("sise00 :" + Serv.it.size());
        } catch (Exception e) {
        }

        return choix;
    }

}
