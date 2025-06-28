import Pokemon.*;
import ru.ifmo.se.pokemon.*;

public class Main {
    public static void main(String[] args) {
        startBattle();
    }

    public static void startBattle(){
        Battle b = new Battle();

        Pokemon p1 = new Bouffalant("", 1);
        Pokemon p2 = new Ninetales("", 1);
        Pokemon p3 = new Togekiss("", 1);
        Pokemon p4 = new Togepi("", 1);
        Pokemon p5 = new Togetic("", 1);
        Pokemon p6 = new Vulpix("", 1);

        b.addAlly(p1);
        b.addAlly(p2);
        b.addAlly(p3);

        b.addFoe(p4);
        b.addFoe(p5);
        b.addFoe(p6);

        b.go();
    }
}