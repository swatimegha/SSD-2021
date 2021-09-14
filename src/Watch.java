public class Watch implements Observer{
    @Override
    public void update(Message m) {
        System.out.println("WatchSubscriber :: " + m.getMessageContent());
    }
}
