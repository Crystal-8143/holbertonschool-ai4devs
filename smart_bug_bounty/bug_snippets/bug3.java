package smart_bug_bounty.bug_snippets;

import java.util.Arrays;

public class bug3 {
    public static double averageRating(int[] ratings) {
        if (ratings == null || ratings.length == 0) {
            throw new IllegalArgumentException("ratings must not be empty");
        }

        int total = 0;
        for (int rating : ratings) {
            total += rating;
        }
        return total / ratings.length;
    }

    public static void main(String[] args) {
        int[] ratings = {4, 5};
        System.out.println("Ratings: " + Arrays.toString(ratings));
        System.out.println("Average: " + averageRating(ratings));
    }
}
