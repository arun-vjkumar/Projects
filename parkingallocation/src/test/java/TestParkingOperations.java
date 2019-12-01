import entity.Allocation;
import org.junit.Assert;
import org.junit.Test;

import java.util.List;

public class TestParkingOperations {

    @Test(expected = IllegalArgumentException.class)
    public void testBasicOperations() {
        ParkingAllocation parkingAllocation =  new ParkingAllocation();
        Assert.assertEquals("Created a parking lot with 6 slots", parkingAllocation.createParkingLot(6));
        parkingAllocation.addAllocation("KA-01-HH-2701", "White");
        parkingAllocation.addAllocation("KA-01-HH-9999", "White");
        parkingAllocation.addAllocation("KA-01-BB-0001", "Black");
        parkingAllocation.addAllocation("KA-01-HH-7777", "Red");

        String curStatus = parkingAllocation.performBasicOperation(BasicOperations.STATUS);
        String expectedStatus = "Slot No. Registration No      Color\n" +
                "    1 KA-01-HH-2701      White\n" +
                "    2 KA-01-HH-9999      White\n" +
                "    3 KA-01-BB-0001      Black\n" +
                "    4 KA-01-HH-7777        Red";
        Assert.assertEquals(expectedStatus, curStatus);

        Assert.assertEquals("Slot number 4 is free \n", parkingAllocation.deAllocate(4));
        parkingAllocation.deAllocate(4);
    }

    @Test
    public void testAdvancedOperations() {
        ParkingAllocation  parkingAllocation =  new ParkingAllocation();
        parkingAllocation.createParkingLot(6);
        parkingAllocation.addAllocation("KA-01-HH-2701", "White");
        parkingAllocation.addAllocation("KA-01-HH-9999", "White");
        parkingAllocation.addAllocation("KA-01-BB-0001", "Black");
        parkingAllocation.addAllocation("KA-01-HH-7777", "Red");
        parkingAllocation.addAllocation("KA-01-HH-2701", "Blue");
        parkingAllocation.addAllocation("KA-01-HH-3141", "Black");
        parkingAllocation.addAllocation("KA-01-P-333", "White");
        parkingAllocation.addAllocation("DL-12-AA-9999", "White");

        List<Allocation> selectedAllocation = parkingAllocation.getAllocationByColor("White");
        Assert.assertEquals(2, selectedAllocation.size());
        Assert.assertEquals("KA-01-HH-2701", selectedAllocation.get(0).getVehicle().getRegistrationNumber());
        Assert.assertEquals(0, parkingAllocation.getAllocationByRegNo("MH-04-AY-1111").size());
    }

}
