
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Scanner;

/**
 * Created by jiebo on 04/01/2018  
 */

public class Sum {
    public static void main(String[] args) {
        List<ArrayList<Integer>> inputList = new ArrayList<ArrayList<Integer>>();
        HashMap<Integer, Integer> inputSize = new HashMap(4);
        Scanner sc = new Scanner(System.in);

        for (int i=0; i<4; i++)
            inputSize.put(i, sc.nextInt());

        for (int i=0; i<4; i++) {
            ArrayList<Integer> setList = new ArrayList();
            for (int j=0; j<inputSize.get(i); j++) {
                setList.add(sc.nextInt());
            }
            inputList.add(setList);
        }

        for (int i=0; i<4; i++) {
            System.out.print("Set " + i + " has ");
            System.out.print(inputList.get(i).toString());
            System.out.println();
        }

        if (!isSumZero(0, 0, 0, 0, inputList))
            System.out.println("No valid set"); 

    }

    private static boolean isSumZero(int a, int b, int c, int d, List<ArrayList<Integer>> inputList) {

        List<Integer> arrayA = inputList.get(0);
        List<Integer> arrayB = inputList.get(1);
        List<Integer> arrayC = inputList.get(2);
        List<Integer> arrayD = inputList.get(3);
        if (arrayA.size() <= a
                || arrayB.size() <= b
                || arrayC.size() <= c
                || arrayD.size() <= d)
            return false;

        if (arrayA.get(a) + arrayB.get(b) + arrayC.get(c) + arrayD.get(d) == 0) {
            System.out.printf("%d %d %d %d \n", arrayA.get(a), arrayB.get(b), arrayC.get(c), arrayD.get(d));
            return true;
        }
        return isSumZero(a+1, b, c, d, inputList)
                || isSumZero(a, b+1, c, d, inputList)
                || isSumZero(a, b, c+1, d, inputList)
                || isSumZero(a, b, c, d+1, inputList);

    }
}
