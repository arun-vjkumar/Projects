package entity;

import java.util.SortedSet;
import java.util.TreeSet;

public class ParkingLot {

    private SortedSet<Integer> freeParkingSlots;

    public ParkingLot(int numOfSlots) {
        this.freeParkingSlots = new TreeSet<>();
        for (int i = 1; i <= numOfSlots; i++)
            this.freeParkingSlots.add(i);
    }

    public Integer getNumberOfFreeParkingSlot() {
        return this.freeParkingSlots.size();
    }

    public Integer getNearestParkingSlot() {
        Integer nearestSlot = null;
        if (this.freeParkingSlots.size() > 0)
            nearestSlot = this.freeParkingSlots.first();
        if (nearestSlot != null)
            this.freeParkingSlots.remove(nearestSlot);
        return nearestSlot;
    }

    public void insertParkingSlot(Integer parkingSlot) {
        this.freeParkingSlots.add(parkingSlot);
    }

}
