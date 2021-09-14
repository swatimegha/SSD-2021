public class Tablet implements Observer{
    @Override
    public void update(Message m) {
        System.out.println("TabletSubscriber :: " + m.getMessageContent());
    }
}
