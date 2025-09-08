package Pokemon;

import Move.FireBlast;
import Move.Overheat;
import Move.Swagger;
import ru.ifmo.se.pokemon.Pokemon;

public class Vulpix extends Pokemon {
     static  double HP = 38;
     static double ATTACK = 41;
     static  double DEFENSE = 40;
     static  double SPECIAL_ATTACK = 50;
     static  double SPECIAL_DEFENCE = 65;
     static  double SPEED = 65;
    public Vulpix(String name, int level) {
        super(name, level);
        setStats(HP, ATTACK, DEFENSE, SPECIAL_ATTACK, SPECIAL_DEFENCE,
                SPEED);
        addMove(new FireBlast());
        addMove(new Overheat());
        addMove(new Swagger());
    }
}

