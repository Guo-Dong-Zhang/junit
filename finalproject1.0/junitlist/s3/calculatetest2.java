package com.junit;

import org.junit.Test;
import static org.junit.Assert.assertEquals;
import org.junit.Test;
import com.java.calculate;
import com.java.calculate2;

public class calculatetest2{
	calculate calculation = new calculate();
	int sum = calculation.sum(8,2);
	int testSum = 10;

	calculate2 calculation2 = new calculate2();
	int sub = calculation2.sub(8,2);
	int testSub = 6;

	@Test
	public void testSum(){
		System.out.println("@Test sum():"+sum+"="+testSum+"\n");
		assertEquals(sum,testSum);
	}	

	@Test
	public void testSub(){
		System.out.println("@Test sub():"+sub+"+"+testSub+"\n");
		assertEquals(sub,testSub);
	}

}

