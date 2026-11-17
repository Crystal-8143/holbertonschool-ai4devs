package smart_bug_bounty.bug_snippets;

import java.util.Arrays;

public class bug6 {
    public static int highestTemperature(int[] readings) {
        if (readings == null || readings.length == 0) {
            throw new IllegalArgumentException("readings must not be empty");
        }

        int highest = 0;
        for (int temperature : readings) {
            if (temperature > highest) {
                highest = temperature;
            }
        }
        return highest;
    }

    public static void main(String[] args) {
        int[] readings = {-7, -2, -5};
        System.out.println("Readings: " + Arrays.toString(readings));
        System.out.println("Highest temperature: " + highestTemperature(readings));
    }
}