public class Phone implements Observer{
    @Override
    public void update(Message m) {
        System.out.println("PhoneSubscriber :: " + m.getMessageContent());
    }
}
