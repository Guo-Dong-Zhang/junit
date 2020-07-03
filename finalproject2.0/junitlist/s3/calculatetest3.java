package com.junit;

import org.junit.Test;
import static org.junit.Assert.assertEquals;
import org.junit.Test;
import com.java.calculate2;
import com.java.calculate3;

public class calculatetest3{
	calculate2 calculation2 = new calculate2();
	int sub = calculation2.sub(8,2);
	int testSub = 6;

	calculate3 calculation3 = new calculate3();
	int multi = calculation3.multi(8,2);
	int testMulti = 16;
	int div = calculation3.div(8,2);
	int testDiv = 4;

	@Test
	public void testsub(){
		System.out.println("@Test sub():"+sub+"="+testSub+"\n");
		assertEquals(sub,testSub);
	}	
	@Test
	public void testdiv(){
		System.out.println("@Test div():"+div+"="+testDiv+"\n");
	       	assertEquals(div,testDiv);	
	}
	@Test 
	public void testmulti(){
		System.out.println("Test multi():"+multi+"="+testMulti+"\n");
		assertEquals(multi,testMulti);
	}
}

