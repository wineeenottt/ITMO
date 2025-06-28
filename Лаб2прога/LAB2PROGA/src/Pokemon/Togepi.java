package Pokemon;
import Move.DazzlingGleam;
import Move.Facade;
import ru.ifmo.se.pokemon.Pokemon;

public class Togepi extends Pokemon {
     static  double HP = 35;
     static  double ATTACK = 20;
     static  double DEFENSE = 65;
     static  double SPECIAL_ATTACK = 40;
     static  double SPECIAL_DEFENCE = 65;
     static  double SPEED = 20;
    public Togepi(String name, int level) {
        super(name, level);
        setStats(HP, ATTACK, DEFENSE, SPECIAL_ATTACK, SPECIAL_DEFENCE,
                SPEED);
        addMove(new DazzlingGleam());
        addMove(new Facade());
    }
}

