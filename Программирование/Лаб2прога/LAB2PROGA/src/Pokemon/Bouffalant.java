package Pokemon;
import Move.*;
import ru.ifmo.se.pokemon.Pokemon;

public final class Bouffalant extends Pokemon {
     static double HP = 95;
    static  double ATTACK = 110;
    static  double DEFENSE = 95;
    static  double SPECIAL_ATTACK = 40;
    static  double SPECIAL_DEFENCE = 95;
     static  double SPEED = 55;
    public Bouffalant(String name, int level) {
        super(name, level);
        setStats(HP, ATTACK, DEFENSE, SPECIAL_ATTACK, SPECIAL_DEFENCE,
                SPEED);
        addMove(new Swagger());
        addMove(new WorkUp());
        addMove(new FocusEnergy());
        addMove(new ScaryFace());
    }
}
