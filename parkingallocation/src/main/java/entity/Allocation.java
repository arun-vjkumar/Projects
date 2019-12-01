package entity;

public class Allocation implements Comparable<Allocation>{
    private Integer parkingSlot;
    private Vehicle vehicle;

    public Allocation(Integer parkingSlot, Vehicle vehicle) {
        this.parkingSlot = parkingSlot;
        this.vehicle = vehicle;
    }

    public Integer getParkingSlot() {
        return parkingSlot;
    }

    public Vehicle getVehicle() {
        return vehicle;
    }

    @Override
    public int compareTo(Allocation allocation) {
        return this.getParkingSlot().compareTo(allocation.getParkingSlot());
    }
}
