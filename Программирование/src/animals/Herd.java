package animals;


import java.util.List;

public class Herd {
    private List<Goat> goats;

    public void increase(List<Goat> goats){
        this.goats.addAll(goats);
        System.out.println("Стадо выросло! Текущее количество "+this.getCountWithoutKill()+" голов");
        System.out.println("Кроме тех коз; которых я убивал на еду в количестве "+this.getCountWithKill());
    }

    public int getCountWithoutKill(){
        int count = 0;
        for(Goat goat: goats){
            if(!goat.getReasonToKill().equals(ReasonToKill.TO_EAT)){
                count++;
            }
        }
        return count;
    }

    public int getCountWithKill(){
        int count = 0;
        for(Goat goat: goats){
            if(goat.getReasonToKill().equals(ReasonToKill.TO_EAT)){
                count++;
            }
        }
        return count;
    }

    public List<Goat> getGoats() {
        return goats;
    }

    public void setGoats(List<Goat> allGoats) {
        this.goats = allGoats;
    }
}
