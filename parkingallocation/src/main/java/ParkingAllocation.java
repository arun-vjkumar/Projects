import entity.Allocation;
import entity.ParkingLot;
import entity.Vehicle;

import java.util.*;
import java.util.stream.Collectors;

public class ParkingAllocation {
    private static Scanner scanner = new Scanner(System.in);
    private List<Allocation> parkingAllocations;
    private ParkingLot parkingLot;

    public String createParkingLot(int numOfSlots) {
        this.parkingAllocations = new ArrayList<>();
        this.parkingLot =  new ParkingLot(numOfSlots);
        return String.format("Created a parking lot with %d slots", numOfSlots);
    }

    public String deAllocate(Integer parkingSlot) {
        Optional<Allocation> allocationToFree = this.parkingAllocations.stream().filter(allocation -> allocation.getParkingSlot().equals(parkingSlot)).findFirst();
        if (allocationToFree.isPresent()) {
            parkingAllocations.remove(allocationToFree.get());
            return String.format("Slot number %d is free \n", allocationToFree.get().getParkingSlot());
        }
        else {
            throw new IllegalArgumentException(String.format("Slot number %d is not Allocated \n", parkingSlot));
        }
    }

    private static String printStatus(List<Allocation> parkingAllocations) {
        Collections.sort(parkingAllocations);
        List<String> statusString = new ArrayList<>();
        if (parkingAllocations.size() > 0) {
            statusString.add(String.format("%5s %10s %10s", "Slot No.", "Registration No", "Color"));

            for (Allocation allocation: parkingAllocations) {
                statusString.add(String.format("%5d %10s %10s", allocation.getParkingSlot(),
                        allocation.getVehicle().getRegistrationNumber(),
                        allocation.getVehicle().getColor()));
            }
        }
        return String.join("\n", statusString);
    }

    public String addAllocation(String registrationNumber, String color) {
        Integer parkingSlot = this.parkingLot.getNearestParkingSlot();
        if (parkingSlot == null)
            return String.format("Sorry, parking lot full");
        else {
            this.parkingAllocations.add(new Allocation(parkingSlot, new Vehicle(registrationNumber, color)));
            return String.format("Allocated slot number: %d \n", parkingSlot);
        }

    }

    public List<Allocation> getAllocationByColor(String color) {
        return this.parkingAllocations
                .stream()
                .filter(allocation -> allocation.getVehicle().getColor().equals(color))
                .collect(Collectors.toList());
    }

    public List<Allocation> getAllocationByRegNo(String registrationNumber) {
        return this.parkingAllocations
                .stream()
                .filter(allocation -> allocation.getVehicle().getRegistrationNumber().equals(registrationNumber))
                .collect(Collectors.toList());
    }

    private static BasicOperations getTypeOfBasicOpertaion(String s) {
        return BasicOperations.valueOf(s);
    }

    private static AdvancedOperations getTypeOfAdvanceOpertaion(String s) {
        return AdvancedOperations.valueOf(s);
    }

    private static String getFormatttedRegNo(List<Allocation> allocations) {
        if (allocations.size() == 0)
            return "Not Found";

        StringBuilder stringToPrint = new StringBuilder();
        for (Allocation allocation: allocations) {
            stringToPrint.append(allocation.getVehicle().getRegistrationNumber());
            stringToPrint.append(", ");
        }

       return stringToPrint.substring(0, stringToPrint.length() - 2);
    }

    private static String getFormattedSlotNo(List<Allocation> allocations) {
        if (allocations.size() == 0)
            return "Not Found";

        StringBuilder stringToPrint = new StringBuilder();
        for (Allocation allocation: allocations) {
            stringToPrint.append(allocation.getParkingSlot().toString());
            stringToPrint.append(", ");
        }

        return stringToPrint.substring(0, stringToPrint.length() - 2);
    }

    public String performAdvanceOperation(AdvancedOperations action) {
        String registrationNumber;
        String color;

        if (parkingLot == null)
            throw new NullPointerException("Parking Lot Is Not Created Yet");

        switch (action) {
            case REGISTRATION_NUMBERS_FOR_CARS_WITH_COLOUR:
                color = scanner.next();
                return getFormatttedRegNo(getAllocationByColor(color));

            case SLOT_NUMBERS_FOR_CARS_WITH_COLOUR:
                color = scanner.next();
                return getFormattedSlotNo(getAllocationByColor(color));


            case SLOT_NUMBER_FOR_REGISTRATION_NUMBER:
                registrationNumber = scanner.next();
                return getFormattedSlotNo(getAllocationByRegNo(registrationNumber));

            default:
                throw new IllegalArgumentException("Command Not Found");
        }
    }

    public String performBasicOperation(BasicOperations action) {
        String registrationNumber;
        String color;

        if (action != BasicOperations.CREATE_PARKING_LOT && parkingLot == null)
            throw new NullPointerException("Parking Lot Is Not Created Yet");


        switch (action) {
            case CREATE_PARKING_LOT:
                int numOfSlots = scanner.nextInt();
                if (this.parkingAllocations != null)
                    throw new IllegalArgumentException("Parking Lot Is Already Created");
                return createParkingLot(numOfSlots);

            case PARK:
                registrationNumber = scanner.next();
                color = scanner.next();
                return addAllocation(registrationNumber, color);

            case LEAVE:
                Integer slotNum = scanner.nextInt();
                this.parkingLot.insertParkingSlot(slotNum);
                return deAllocate(slotNum);

            case STATUS:
                return printStatus(this.parkingAllocations);

            default:
                throw new IllegalArgumentException("Command Not Found");

        }
    }

    public static void main(String[] args) {
        String cmd;
        ParkingAllocation parkingAllocation =  new ParkingAllocation();
        List<String> basicOperations = Arrays.stream(BasicOperations.values()).map(Objects::toString).collect(Collectors.toList());
        List<String> advancedOpertaions = Arrays.stream(AdvancedOperations.values()).map(Objects::toString).collect(Collectors.toList());

        while (true) {
            try {
                cmd = scanner.next().toUpperCase();
                if (basicOperations.contains(cmd)) {
                    System.out.println(parkingAllocation.performBasicOperation(getTypeOfBasicOpertaion(cmd)));
                }

                if (advancedOpertaions.contains(cmd)) {
                    System.out.println(parkingAllocation.performAdvanceOperation(getTypeOfAdvanceOpertaion(cmd)));
                }
            } catch (NullPointerException | IllegalArgumentException e) {
                System.out.println(e.getMessage());
            }
        }
    }
}
