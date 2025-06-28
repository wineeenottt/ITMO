package Move;

import ru.ifmo.se.pokemon.Pokemon;
import ru.ifmo.se.pokemon.SpecialMove;
import ru.ifmo.se.pokemon.Stat;
import ru.ifmo.se.pokemon.Type;

public class DazzlingGleam extends SpecialMove {
     static  Type TYPE = Type.FAIRY;
     static  double POWER = 80;
     static  double ACCURACY = 100;

    public DazzlingGleam() {
        super(TYPE, POWER, ACCURACY);
    }
    @Override
    protected String describe(){
        return "Применил Dazzling Gleam";
    }
    @Override
    protected void applySelfDamage(Pokemon opp, double damage) {
        opp.setMod(Stat.HP, (int) damage);
    }
}

