package Move;

import ru.ifmo.se.pokemon.Pokemon;
import ru.ifmo.se.pokemon.Stat;
import ru.ifmo.se.pokemon.StatusMove;
import ru.ifmo.se.pokemon.Type;

public class FocusEnergy extends StatusMove {
    static Type TYPE = Type.FIRE;
    static double POWER = 0;
    static double ACCURACY = 0;

    public FocusEnergy() {
        super(TYPE, POWER, ACCURACY);
    }

    @Override
    protected String describe() {
        return "Применил Focus Energy";
    }

    @Override
    protected void applySelfEffects(Pokemon p) {
        p.setMod(Stat.SPECIAL_ATTACK, +1);
    }
}
