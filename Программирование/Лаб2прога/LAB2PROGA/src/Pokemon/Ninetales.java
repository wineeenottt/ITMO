package Pokemon;
import Move.DreamEater;

public final class Ninetales extends Vulpix {
     static  double HP = 73;
     static  double ATTACK = 76;
    static double DEFENSE = 75;
     static  double SPECIAL_ATTACK = 81;
    static  double SPECIAL_DEFENCE = 100;
   static  double SPEED = 100;
    public Ninetales(String name, int level) {
        super(name, level);
        setStats(HP, ATTACK, DEFENSE, SPECIAL_ATTACK, SPECIAL_DEFENCE,
                SPEED);
        addMove(new DreamEater());
    }
}
