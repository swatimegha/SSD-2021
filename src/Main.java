public class Main
{
    public static void main(String[] args)
    {
        Phone p1 = new Phone();
        Tablet t1 = new Tablet();
        Watch w1 = new Watch();

        Weatherstation p = new Weatherstation();

        p.attach(p1);
        p.attach(t1);

        p.notifyUpdate(new Message("Got Message No 1"));

        p.detach(p1);
        p.attach(w1);

        p.notifyUpdate(new Message("Got Message No 2")); //p2 and w2 will receive the update
    }
}