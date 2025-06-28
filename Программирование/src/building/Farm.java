package building;
public abstract class Farm extends Building implements Breakable{

    public Farm(String name) {
        super(name);
    }

    public abstract void produceProducts();
}
