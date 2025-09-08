package Move;

import ru.ifmo.se.pokemon.Pokemon;
import ru.ifmo.se.pokemon.SpecialMove;
import ru.ifmo.se.pokemon.Stat;
import ru.ifmo.se.pokemon.Type;

public class Overheat extends SpecialMove {
    static Type TYPE = Type.FIRE;
    static double POWER = 130;
    static  double ACCURACY = 90;

    public Overheat() {
        super(TYPE, POWER, ACCURACY);
    }
    @Override
    protected String describe() {
        return "Применил Overheat";
    }
    @Override
    protected void applySelfEffects(Pokemon p) {
        // Снижение специальной атаки на 2 этапа
        p.setMod(Stat.SPECIAL_ATTACK, -2);
    }
}
