package com.pekingstyle.curvemaker;

import java.util.HashMap;
import java.util.Iterator;
import java.util.Map.Entry;
import java.util.Set;

public class InterpolateHandler {

	/*
	 * �ж�ʹ�����ֲ�ֵ������ 1. ���Բ�ֵ 2. �������ղ�ֵ 3. �������ز�ֵ ʹ�ö�Ӧ��ϵ�������ò�ͬ�Ĳ�ֵ����
	 */
	public static HashMap<Double, Double> point = new HashMap<Double,Double>();

	public static double[] x;
	public static String[] y;

	public static void main(String args[]) {

		doLiner(GetPoints.initPointArray(point));

	}

	private static void doLiner(HashMap<Double, Double> point) {
		Iterator i = point.entrySet().iterator();
		
		while(i.hasNext()){
		Entry e =(java.util.Map.Entry) i.next();
		System.out.println(e.getKey());
		}
	}


		
	
}
