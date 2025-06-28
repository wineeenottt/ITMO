package Pokemon;

import Move.DoubleTeam;


public final class Togekiss extends Togetic {
    static double HP = 85;
    static double ATTACK = 50;
    static double DEFENSE = 95;
    static double SPECIAL_ATTACK = 120;
    static double SPECIAL_DEFENCE = 115;
    static double SPEED = 80;

    public Togekiss(String name, int level) {
        super(name, level);
        setStats(HP, ATTACK, DEFENSE, SPECIAL_ATTACK, SPECIAL_DEFENCE,
                SPEED);
        addMove(new DoubleTeam());
    }
}