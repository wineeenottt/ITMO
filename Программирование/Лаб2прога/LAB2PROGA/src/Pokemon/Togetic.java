package Pokemon;

import Move.AncientPower;

public class Togetic extends Togepi {
     static  double HP = 55;
     static  double ATTACK = 40;
     static  double DEFENSE = 85;
     static  double SPECIAL_ATTACK = 80;
     static  double SPECIAL_DEFENCE = 105;
     static  double SPEED = 40;
    public Togetic(String name, int level) {
        super(name, level);
        setStats(HP, ATTACK, DEFENSE, SPECIAL_ATTACK, SPECIAL_DEFENCE,
                SPEED);
        addMove(new AncientPower());
    }
}


