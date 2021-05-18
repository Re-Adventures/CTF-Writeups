
rev:     file format elf64-x86-64


Disassembly of section .init:

0000000000001000 <_init>:
    1000:	f3 0f 1e fa          	endbr64 
    1004:	48 83 ec 08          	sub    rsp,0x8
    1008:	48 8b 05 d9 7f 00 00 	mov    rax,QWORD PTR [rip+0x7fd9]        # 8fe8 <__gmon_start__>
    100f:	48 85 c0             	test   rax,rax
    1012:	74 02                	je     1016 <_init+0x16>
    1014:	ff d0                	call   rax
    1016:	48 83 c4 08          	add    rsp,0x8
    101a:	c3                   	ret    

Disassembly of section .plt:

0000000000001020 <.plt>:
    1020:	ff 35 8a 7f 00 00    	push   QWORD PTR [rip+0x7f8a]        # 8fb0 <_GLOBAL_OFFSET_TABLE_+0x8>
    1026:	f2 ff 25 8b 7f 00 00 	bnd jmp QWORD PTR [rip+0x7f8b]        # 8fb8 <_GLOBAL_OFFSET_TABLE_+0x10>
    102d:	0f 1f 00             	nop    DWORD PTR [rax]
    1030:	f3 0f 1e fa          	endbr64 
    1034:	68 00 00 00 00       	push   0x0
    1039:	f2 e9 e1 ff ff ff    	bnd jmp 1020 <.plt>
    103f:	90                   	nop
    1040:	f3 0f 1e fa          	endbr64 
    1044:	68 01 00 00 00       	push   0x1
    1049:	f2 e9 d1 ff ff ff    	bnd jmp 1020 <.plt>
    104f:	90                   	nop
    1050:	f3 0f 1e fa          	endbr64 
    1054:	68 02 00 00 00       	push   0x2
    1059:	f2 e9 c1 ff ff ff    	bnd jmp 1020 <.plt>
    105f:	90                   	nop

Disassembly of section .plt.got:

0000000000001060 <__cxa_finalize@plt>:
    1060:	f3 0f 1e fa          	endbr64 
    1064:	f2 ff 25 8d 7f 00 00 	bnd jmp QWORD PTR [rip+0x7f8d]        # 8ff8 <__cxa_finalize@GLIBC_2.2.5>
    106b:	0f 1f 44 00 00       	nop    DWORD PTR [rax+rax*1+0x0]

Disassembly of section .plt.sec:

0000000000001070 <puts@plt>:
    1070:	f3 0f 1e fa          	endbr64 
    1074:	f2 ff 25 45 7f 00 00 	bnd jmp QWORD PTR [rip+0x7f45]        # 8fc0 <puts@GLIBC_2.2.5>
    107b:	0f 1f 44 00 00       	nop    DWORD PTR [rax+rax*1+0x0]

0000000000001080 <__stack_chk_fail@plt>:
    1080:	f3 0f 1e fa          	endbr64 
    1084:	f2 ff 25 3d 7f 00 00 	bnd jmp QWORD PTR [rip+0x7f3d]        # 8fc8 <__stack_chk_fail@GLIBC_2.4>
    108b:	0f 1f 44 00 00       	nop    DWORD PTR [rax+rax*1+0x0]

0000000000001090 <read@plt>:
    1090:	f3 0f 1e fa          	endbr64 
    1094:	f2 ff 25 35 7f 00 00 	bnd jmp QWORD PTR [rip+0x7f35]        # 8fd0 <read@GLIBC_2.2.5>
    109b:	0f 1f 44 00 00       	nop    DWORD PTR [rax+rax*1+0x0]

Disassembly of section .text:

00000000000010a0 <_start>:
    10a0:	f3 0f 1e fa          	endbr64 
    10a4:	31 ed                	xor    ebp,ebp
    10a6:	49 89 d1             	mov    r9,rdx
    10a9:	5e                   	pop    rsi
    10aa:	48 89 e2             	mov    rdx,rsp
    10ad:	48 83 e4 f0          	and    rsp,0xfffffffffffffff0
    10b1:	50                   	push   rax
    10b2:	54                   	push   rsp
    10b3:	4c 8d 05 c6 36 00 00 	lea    r8,[rip+0x36c6]        # 4780 <__libc_csu_fini>
    10ba:	48 8d 0d 4f 36 00 00 	lea    rcx,[rip+0x364f]        # 4710 <__libc_csu_init>
    10c1:	48 8d 3d 13 23 00 00 	lea    rdi,[rip+0x2313]        # 33db <main>
    10c8:	ff 15 12 7f 00 00    	call   QWORD PTR [rip+0x7f12]        # 8fe0 <__libc_start_main@GLIBC_2.2.5>
    10ce:	f4                   	hlt    
    10cf:	90                   	nop

00000000000010d0 <deregister_tm_clones>:
    10d0:	48 8d 3d 39 7f 00 00 	lea    rdi,[rip+0x7f39]        # 9010 <__TMC_END__>
    10d7:	48 8d 05 32 7f 00 00 	lea    rax,[rip+0x7f32]        # 9010 <__TMC_END__>
    10de:	48 39 f8             	cmp    rax,rdi
    10e1:	74 15                	je     10f8 <deregister_tm_clones+0x28>
    10e3:	48 8b 05 ee 7e 00 00 	mov    rax,QWORD PTR [rip+0x7eee]        # 8fd8 <_ITM_deregisterTMCloneTable>
    10ea:	48 85 c0             	test   rax,rax
    10ed:	74 09                	je     10f8 <deregister_tm_clones+0x28>
    10ef:	ff e0                	jmp    rax
    10f1:	0f 1f 80 00 00 00 00 	nop    DWORD PTR [rax+0x0]
    10f8:	c3                   	ret    
    10f9:	0f 1f 80 00 00 00 00 	nop    DWORD PTR [rax+0x0]

0000000000001100 <register_tm_clones>:
    1100:	48 8d 3d 09 7f 00 00 	lea    rdi,[rip+0x7f09]        # 9010 <__TMC_END__>
    1107:	48 8d 35 02 7f 00 00 	lea    rsi,[rip+0x7f02]        # 9010 <__TMC_END__>
    110e:	48 29 fe             	sub    rsi,rdi
    1111:	48 89 f0             	mov    rax,rsi
    1114:	48 c1 ee 3f          	shr    rsi,0x3f
    1118:	48 c1 f8 03          	sar    rax,0x3
    111c:	48 01 c6             	add    rsi,rax
    111f:	48 d1 fe             	sar    rsi,1
    1122:	74 14                	je     1138 <register_tm_clones+0x38>
    1124:	48 8b 05 c5 7e 00 00 	mov    rax,QWORD PTR [rip+0x7ec5]        # 8ff0 <_ITM_registerTMCloneTable>
    112b:	48 85 c0             	test   rax,rax
    112e:	74 08                	je     1138 <register_tm_clones+0x38>
    1130:	ff e0                	jmp    rax
    1132:	66 0f 1f 44 00 00    	nop    WORD PTR [rax+rax*1+0x0]
    1138:	c3                   	ret    
    1139:	0f 1f 80 00 00 00 00 	nop    DWORD PTR [rax+0x0]

0000000000001140 <__do_global_dtors_aux>:
    1140:	f3 0f 1e fa          	endbr64 
    1144:	80 3d c5 7e 00 00 00 	cmp    BYTE PTR [rip+0x7ec5],0x0        # 9010 <__TMC_END__>
    114b:	75 2b                	jne    1178 <__do_global_dtors_aux+0x38>
    114d:	55                   	push   rbp
    114e:	48 83 3d a2 7e 00 00 	cmp    QWORD PTR [rip+0x7ea2],0x0        # 8ff8 <__cxa_finalize@GLIBC_2.2.5>
    1155:	00 
    1156:	48 89 e5             	mov    rbp,rsp
    1159:	74 0c                	je     1167 <__do_global_dtors_aux+0x27>
    115b:	48 8b 3d a6 7e 00 00 	mov    rdi,QWORD PTR [rip+0x7ea6]        # 9008 <__dso_handle>
    1162:	e8 f9 fe ff ff       	call   1060 <__cxa_finalize@plt>
    1167:	e8 64 ff ff ff       	call   10d0 <deregister_tm_clones>
    116c:	c6 05 9d 7e 00 00 01 	mov    BYTE PTR [rip+0x7e9d],0x1        # 9010 <__TMC_END__>
    1173:	5d                   	pop    rbp
    1174:	c3                   	ret    
    1175:	0f 1f 00             	nop    DWORD PTR [rax]
    1178:	c3                   	ret    
    1179:	0f 1f 80 00 00 00 00 	nop    DWORD PTR [rax+0x0]

0000000000001180 <frame_dummy>:
    1180:	f3 0f 1e fa          	endbr64 
    1184:	e9 77 ff ff ff       	jmp    1100 <register_tm_clones>

0000000000001189 <f122323>:
    1189:	f3 0f 1e fa          	endbr64 
    118d:	55                   	push   rbp
    118e:	48 89 e5             	mov    rbp,rsp
    1191:	89 f8                	mov    eax,edi
    1193:	88 45 fc             	mov    BYTE PTR [rbp-0x4],al
    1196:	0f be 45 fc          	movsx  eax,BYTE PTR [rbp-0x4]
    119a:	c1 e0 04             	shl    eax,0x4
    119d:	0f b6 d0             	movzx  edx,al
    11a0:	0f b6 45 fc          	movzx  eax,BYTE PTR [rbp-0x4]
    11a4:	c0 f8 04             	sar    al,0x4
    11a7:	0f be c0             	movsx  eax,al
    11aa:	01 d0                	add    eax,edx
    11ac:	83 f8 46             	cmp    eax,0x46
    11af:	0f 94 c0             	sete   al
    11b2:	5d                   	pop    rbp
    11b3:	c3                   	ret    

00000000000011b4 <f7093176>:
    11b4:	f3 0f 1e fa          	endbr64 
    11b8:	55                   	push   rbp
    11b9:	48 89 e5             	mov    rbp,rsp
    11bc:	89 f8                	mov    eax,edi
    11be:	88 45 fc             	mov    BYTE PTR [rbp-0x4],al
    11c1:	0f be 45 fc          	movsx  eax,BYTE PTR [rbp-0x4]
    11c5:	c1 e0 04             	shl    eax,0x4
    11c8:	0f b6 d0             	movzx  edx,al
    11cb:	0f b6 45 fc          	movzx  eax,BYTE PTR [rbp-0x4]
    11cf:	c0 f8 04             	sar    al,0x4
    11d2:	0f be c0             	movsx  eax,al
    11d5:	01 d0                	add    eax,edx
    11d7:	83 f8 16             	cmp    eax,0x16
    11da:	0f 94 c0             	sete   al
    11dd:	5d                   	pop    rbp
    11de:	c3                   	ret    

00000000000011df <f2267326>:
    11df:	f3 0f 1e fa          	endbr64 
    11e3:	55                   	push   rbp
    11e4:	48 89 e5             	mov    rbp,rsp
    11e7:	89 f8                	mov    eax,edi
    11e9:	88 45 fc             	mov    BYTE PTR [rbp-0x4],al
    11ec:	0f be 45 fc          	movsx  eax,BYTE PTR [rbp-0x4]
    11f0:	c1 e0 04             	shl    eax,0x4
    11f3:	0f b6 d0             	movzx  edx,al
    11f6:	0f b6 45 fc          	movzx  eax,BYTE PTR [rbp-0x4]
    11fa:	c0 f8 04             	sar    al,0x4
    11fd:	0f be c0             	movsx  eax,al
    1200:	01 d0                	add    eax,edx
    1202:	83 f8 27             	cmp    eax,0x27
    1205:	0f 94 c0             	sete   al
    1208:	5d                   	pop    rbp
    1209:	c3                   	ret    

000000000000120a <f3113161>:
    120a:	f3 0f 1e fa          	endbr64 
    120e:	55                   	push   rbp
    120f:	48 89 e5             	mov    rbp,rsp
    1212:	89 f8                	mov    eax,edi
    1214:	88 45 fc             	mov    BYTE PTR [rbp-0x4],al
    1217:	0f be 45 fc          	movsx  eax,BYTE PTR [rbp-0x4]
    121b:	c1 e0 04             	shl    eax,0x4
    121e:	0f b6 d0             	movzx  edx,al
    1221:	0f b6 45 fc          	movzx  eax,BYTE PTR [rbp-0x4]
    1225:	c0 f8 04             	sar    al,0x4
    1228:	0f be c0             	movsx  eax,al
    122b:	01 d0                	add    eax,edx
    122d:	3d b6 00 00 00       	cmp    eax,0xb6
    1232:	0f 94 c0             	sete   al
    1235:	5d                   	pop    rbp
    1236:	c3                   	ret    

0000000000001237 <f6910364>:
    1237:	f3 0f 1e fa          	endbr64 
    123b:	55                   	push   rbp
    123c:	48 89 e5             	mov    rbp,rsp
    123f:	89 f8                	mov    eax,edi
    1241:	88 45 fc             	mov    BYTE PTR [rbp-0x4],al
    1244:	0f be 45 fc          	movsx  eax,BYTE PTR [rbp-0x4]
    1248:	c1 e0 04             	shl    eax,0x4
    124b:	0f b6 d0             	movzx  edx,al
    124e:	0f b6 45 fc          	movzx  eax,BYTE PTR [rbp-0x4]
    1252:	c0 f8 04             	sar    al,0x4
    1255:	0f be c0             	movsx  eax,al
    1258:	01 d0                	add    eax,edx
    125a:	83 f8 34             	cmp    eax,0x34
    125d:	0f 94 c0             	sete   al
    1260:	5d                   	pop    rbp
    1261:	c3                   	ret    

0000000000001262 <f4838080>:
    1262:	f3 0f 1e fa          	endbr64 
    1266:	55                   	push   rbp
    1267:	48 89 e5             	mov    rbp,rsp
    126a:	89 f8                	mov    eax,edi
    126c:	88 45 fc             	mov    BYTE PTR [rbp-0x4],al
    126f:	0f be 45 fc          	movsx  eax,BYTE PTR [rbp-0x4]
    1273:	c1 e0 04             	shl    eax,0x4
    1276:	0f b6 d0             	movzx  edx,al
    1279:	0f b6 45 fc          	movzx  eax,BYTE PTR [rbp-0x4]
    127d:	c0 f8 04             	sar    al,0x4
    1280:	0f be c0             	movsx  eax,al
    1283:	01 d0                	add    eax,edx
    1285:	3d f4 00 00 00       	cmp    eax,0xf4
    128a:	0f 94 c0             	sete   al
    128d:	5d                   	pop    rbp
    128e:	c3                   	ret    

000000000000128f <f3576179>:
    128f:	f3 0f 1e fa          	endbr64 
    1293:	55                   	push   rbp
    1294:	48 89 e5             	mov    rbp,rsp
    1297:	89 f8                	mov    eax,edi
    1299:	88 45 fc             	mov    BYTE PTR [rbp-0x4],al
    129c:	0f be 45 fc          	movsx  eax,BYTE PTR [rbp-0x4]
    12a0:	c1 e0 04             	shl    eax,0x4
    12a3:	0f b6 d0             	movzx  edx,al
    12a6:	0f b6 45 fc          	movzx  eax,BYTE PTR [rbp-0x4]
    12aa:	c0 f8 04             	sar    al,0x4
    12ad:	0f be c0             	movsx  eax,al
    12b0:	01 d0                	add    eax,edx
    12b2:	3d e4 00 00 00       	cmp    eax,0xe4
    12b7:	0f 94 c0             	sete   al
    12ba:	5d                   	pop    rbp
    12bb:	c3                   	ret    

00000000000012bc <f1715128>:
    12bc:	f3 0f 1e fa          	endbr64 
    12c0:	55                   	push   rbp
    12c1:	48 89 e5             	mov    rbp,rsp
    12c4:	89 f8                	mov    eax,edi
    12c6:	88 45 fc             	mov    BYTE PTR [rbp-0x4],al
    12c9:	0f be 45 fc          	movsx  eax,BYTE PTR [rbp-0x4]
    12cd:	c1 e0 04             	shl    eax,0x4
    12d0:	0f b6 d0             	movzx  edx,al
    12d3:	0f b6 45 fc          	movzx  eax,BYTE PTR [rbp-0x4]
    12d7:	c0 f8 04             	sar    al,0x4
    12da:	0f be c0             	movsx  eax,al
    12dd:	01 d0                	add    eax,edx
    12df:	3d b7 00 00 00       	cmp    eax,0xb7
    12e4:	0f 94 c0             	sete   al
    12e7:	5d                   	pop    rbp
    12e8:	c3                   	ret    

00000000000012e9 <f4029468>:
    12e9:	f3 0f 1e fa          	endbr64 
    12ed:	55                   	push   rbp
    12ee:	48 89 e5             	mov    rbp,rsp
    12f1:	89 f8                	mov    eax,edi
    12f3:	88 45 fc             	mov    BYTE PTR [rbp-0x4],al
    12f6:	0f be 45 fc          	movsx  eax,BYTE PTR [rbp-0x4]
    12fa:	c1 e0 04             	shl    eax,0x4
    12fd:	0f b6 d0             	movzx  edx,al
    1300:	0f b6 45 fc          	movzx  eax,BYTE PTR [rbp-0x4]
    1304:	c0 f8 04             	sar    al,0x4
    1307:	0f be c0             	movsx  eax,al
    130a:	01 d0                	add    eax,edx
    130c:	83 f8 43             	cmp    eax,0x43
    130f:	0f 94 c0             	sete   al
    1312:	5d                   	pop    rbp
    1313:	c3                   	ret    

0000000000001314 <f5723857>:
    1314:	f3 0f 1e fa          	endbr64 
    1318:	55                   	push   rbp
    1319:	48 89 e5             	mov    rbp,rsp
    131c:	89 f8                	mov    eax,edi
    131e:	88 45 fc             	mov    BYTE PTR [rbp-0x4],al
    1321:	0f be 45 fc          	movsx  eax,BYTE PTR [rbp-0x4]
    1325:	c1 e0 04             	shl    eax,0x4
    1328:	0f b6 d0             	movzx  edx,al
    132b:	0f b6 45 fc          	movzx  eax,BYTE PTR [rbp-0x4]
    132f:	c0 f8 04             	sar    al,0x4
    1332:	0f be c0             	movsx  eax,al
    1335:	01 d0                	add    eax,edx
    1337:	83 f8 27             	cmp    eax,0x27
    133a:	0f 94 c0             	sete   al
    133d:	5d                   	pop    rbp
    133e:	c3                   	ret    

000000000000133f <f5333530>:
    133f:	f3 0f 1e fa          	endbr64 
    1343:	55                   	push   rbp
    1344:	48 89 e5             	mov    rbp,rsp
    1347:	89 f8                	mov    eax,edi
    1349:	88 45 fc             	mov    BYTE PTR [rbp-0x4],al
    134c:	0f be 45 fc          	movsx  eax,BYTE PTR [rbp-0x4]
    1350:	c1 e0 04             	shl    eax,0x4
    1353:	0f b6 d0             	movzx  edx,al
    1356:	0f b6 45 fc          	movzx  eax,BYTE PTR [rbp-0x4]
    135a:	c0 f8 04             	sar    al,0x4
    135d:	0f be c0             	movsx  eax,al
    1360:	01 d0                	add    eax,edx
    1362:	83 f8 33             	cmp    eax,0x33
    1365:	0f 94 c0             	sete   al
    1368:	5d                   	pop    rbp
    1369:	c3                   	ret    

000000000000136a <f2200656>:
    136a:	f3 0f 1e fa          	endbr64 
    136e:	55                   	push   rbp
    136f:	48 89 e5             	mov    rbp,rsp
    1372:	89 f8                	mov    eax,edi
    1374:	88 45 fc             	mov    BYTE PTR [rbp-0x4],al
    1377:	0f be 45 fc          	movsx  eax,BYTE PTR [rbp-0x4]
    137b:	c1 e0 04             	shl    eax,0x4
    137e:	0f b6 d0             	movzx  edx,al
    1381:	0f b6 45 fc          	movzx  eax,BYTE PTR [rbp-0x4]
    1385:	c0 f8 04             	sar    al,0x4
    1388:	0f be c0             	movsx  eax,al
    138b:	01 d0                	add    eax,edx
    138d:	3d f5 00 00 00       	cmp    eax,0xf5
    1392:	0f 94 c0             	sete   al
    1395:	5d                   	pop    rbp
    1396:	c3                   	ret    

0000000000001397 <f5832933>:
    1397:	f3 0f 1e fa          	endbr64 
    139b:	55                   	push   rbp
    139c:	48 89 e5             	mov    rbp,rsp
    139f:	89 f8                	mov    eax,edi
    13a1:	88 45 fc             	mov    BYTE PTR [rbp-0x4],al
    13a4:	0f be 45 fc          	movsx  eax,BYTE PTR [rbp-0x4]
    13a8:	c1 e0 04             	shl    eax,0x4
    13ab:	0f b6 d0             	movzx  edx,al
    13ae:	0f b6 45 fc          	movzx  eax,BYTE PTR [rbp-0x4]
    13b2:	c0 f8 04             	sar    al,0x4
    13b5:	0f be c0             	movsx  eax,al
    13b8:	01 d0                	add    eax,edx
    13ba:	3d 97 00 00 00       	cmp    eax,0x97
    13bf:	0f 94 c0             	sete   al
    13c2:	5d                   	pop    rbp
    13c3:	c3                   	ret    

00000000000013c4 <f162470>:
    13c4:	f3 0f 1e fa          	endbr64 
    13c8:	55                   	push   rbp
    13c9:	48 89 e5             	mov    rbp,rsp
    13cc:	89 f8                	mov    eax,edi
    13ce:	88 45 fc             	mov    BYTE PTR [rbp-0x4],al
    13d1:	0f be 45 fc          	movsx  eax,BYTE PTR [rbp-0x4]
    13d5:	c1 e0 04             	shl    eax,0x4
    13d8:	0f b6 d0             	movzx  edx,al
    13db:	0f b6 45 fc          	movzx  eax,BYTE PTR [rbp-0x4]
    13df:	c0 f8 04             	sar    al,0x4
    13e2:	0f be c0             	movsx  eax,al
    13e5:	01 d0                	add    eax,edx
    13e7:	83 f8 03             	cmp    eax,0x3
    13ea:	0f 94 c0             	sete   al
    13ed:	5d                   	pop    rbp
    13ee:	c3                   	ret    

00000000000013ef <f9363706>:
    13ef:	f3 0f 1e fa          	endbr64 
    13f3:	55                   	push   rbp
    13f4:	48 89 e5             	mov    rbp,rsp
    13f7:	89 f8                	mov    eax,edi
    13f9:	88 45 fc             	mov    BYTE PTR [rbp-0x4],al
    13fc:	0f be 45 fc          	movsx  eax,BYTE PTR [rbp-0x4]
    1400:	c1 e0 04             	shl    eax,0x4
    1403:	0f b6 d0             	movzx  edx,al
    1406:	0f b6 45 fc          	movzx  eax,BYTE PTR [rbp-0x4]
    140a:	c0 f8 04             	sar    al,0x4
    140d:	0f be c0             	movsx  eax,al
    1410:	01 d0                	add    eax,edx
    1412:	83 f8 57             	cmp    eax,0x57
    1415:	0f 94 c0             	sete   al
    1418:	5d                   	pop    rbp
    1419:	c3                   	ret    

000000000000141a <f8682222>:
    141a:	f3 0f 1e fa          	endbr64 
    141e:	55                   	push   rbp
    141f:	48 89 e5             	mov    rbp,rsp
    1422:	89 f8                	mov    eax,edi
    1424:	88 45 fc             	mov    BYTE PTR [rbp-0x4],al
    1427:	0f be 45 fc          	movsx  eax,BYTE PTR [rbp-0x4]
    142b:	c1 e0 04             	shl    eax,0x4
    142e:	0f b6 d0             	movzx  edx,al
    1431:	0f b6 45 fc          	movzx  eax,BYTE PTR [rbp-0x4]
    1435:	c0 f8 04             	sar    al,0x4
    1438:	0f be c0             	movsx  eax,al
    143b:	01 d0                	add    eax,edx
    143d:	3d f5 00 00 00       	cmp    eax,0xf5
    1442:	0f 94 c0             	sete   al
    1445:	5d                   	pop    rbp
    1446:	c3                   	ret    

0000000000001447 <f5150019>:
    1447:	f3 0f 1e fa          	endbr64 
    144b:	55                   	push   rbp
    144c:	48 89 e5             	mov    rbp,rsp
    144f:	89 f8                	mov    eax,edi
    1451:	88 45 fc             	mov    BYTE PTR [rbp-0x4],al
    1454:	0f be 45 fc          	movsx  eax,BYTE PTR [rbp-0x4]
    1458:	c1 e0 04             	shl    eax,0x4
    145b:	0f b6 d0             	movzx  edx,al
    145e:	0f b6 45 fc          	movzx  eax,BYTE PTR [rbp-0x4]
    1462:	c0 f8 04             	sar    al,0x4
    1465:	0f be c0             	movsx  eax,al
    1468:	01 d0                	add    eax,edx
    146a:	83 f8 27             	cmp    eax,0x27
    146d:	0f 94 c0             	sete   al
    1470:	5d                   	pop    rbp
    1471:	c3                   	ret    

0000000000001472 <f846013>:
    1472:	f3 0f 1e fa          	endbr64 
    1476:	55                   	push   rbp
    1477:	48 89 e5             	mov    rbp,rsp
    147a:	89 f8                	mov    eax,edi
    147c:	88 45 fc             	mov    BYTE PTR [rbp-0x4],al
    147f:	0f be 45 fc          	movsx  eax,BYTE PTR [rbp-0x4]
    1483:	c1 e0 04             	shl    eax,0x4
    1486:	0f b6 d0             	movzx  edx,al
    1489:	0f b6 45 fc          	movzx  eax,BYTE PTR [rbp-0x4]
    148d:	c0 f8 04             	sar    al,0x4
    1490:	0f be c0             	movsx  eax,al
    1493:	01 d0                	add    eax,edx
    1495:	83 f8 33             	cmp    eax,0x33
    1498:	0f 94 c0             	sete   al
    149b:	5d                   	pop    rbp
    149c:	c3                   	ret    

000000000000149d <f1205907>:
    149d:	f3 0f 1e fa          	endbr64 
    14a1:	55                   	push   rbp
    14a2:	48 89 e5             	mov    rbp,rsp
    14a5:	89 f8                	mov    eax,edi
    14a7:	88 45 fc             	mov    BYTE PTR [rbp-0x4],al
    14aa:	0f be 45 fc          	movsx  eax,BYTE PTR [rbp-0x4]
    14ae:	c1 e0 04             	shl    eax,0x4
    14b1:	0f b6 d0             	movzx  edx,al
    14b4:	0f b6 45 fc          	movzx  eax,BYTE PTR [rbp-0x4]
    14b8:	c0 f8 04             	sar    al,0x4
    14bb:	0f be c0             	movsx  eax,al
    14be:	01 d0                	add    eax,edx
    14c0:	83 f8 43             	cmp    eax,0x43
    14c3:	0f 94 c0             	sete   al
    14c6:	5d                   	pop    rbp
    14c7:	c3                   	ret    

00000000000014c8 <f6037610>:
    14c8:	f3 0f 1e fa          	endbr64 
    14cc:	55                   	push   rbp
    14cd:	48 89 e5             	mov    rbp,rsp
    14d0:	89 f8                	mov    eax,edi
    14d2:	88 45 fc             	mov    BYTE PTR [rbp-0x4],al
    14d5:	0f be 45 fc          	movsx  eax,BYTE PTR [rbp-0x4]
    14d9:	c1 e0 04             	shl    eax,0x4
    14dc:	0f b6 d0             	movzx  edx,al
    14df:	0f b6 45 fc          	movzx  eax,BYTE PTR [rbp-0x4]
    14e3:	c0 f8 04             	sar    al,0x4
    14e6:	0f be c0             	movsx  eax,al
    14e9:	01 d0                	add    eax,edx
    14eb:	3d c6 00 00 00       	cmp    eax,0xc6
    14f0:	0f 94 c0             	sete   al
    14f3:	5d                   	pop    rbp
    14f4:	c3                   	ret    

00000000000014f5 <f9848350>:
    14f5:	f3 0f 1e fa          	endbr64 
    14f9:	55                   	push   rbp
    14fa:	48 89 e5             	mov    rbp,rsp
    14fd:	89 f8                	mov    eax,edi
    14ff:	88 45 fc             	mov    BYTE PTR [rbp-0x4],al
    1502:	0f be 45 fc          	movsx  eax,BYTE PTR [rbp-0x4]
    1506:	c1 e0 04             	shl    eax,0x4
    1509:	0f b6 d0             	movzx  edx,al
    150c:	0f b6 45 fc          	movzx  eax,BYTE PTR [rbp-0x4]
    1510:	c0 f8 04             	sar    al,0x4
    1513:	0f be c0             	movsx  eax,al
    1516:	01 d0                	add    eax,edx
    1518:	3d c6 00 00 00       	cmp    eax,0xc6
    151d:	0f 94 c0             	sete   al
    1520:	5d                   	pop    rbp
    1521:	c3                   	ret    

0000000000001522 <f6824915>:
    1522:	f3 0f 1e fa          	endbr64 
    1526:	55                   	push   rbp
    1527:	48 89 e5             	mov    rbp,rsp
    152a:	89 f8                	mov    eax,edi
    152c:	88 45 fc             	mov    BYTE PTR [rbp-0x4],al
    152f:	0f be 45 fc          	movsx  eax,BYTE PTR [rbp-0x4]
    1533:	c1 e0 04             	shl    eax,0x4
    1536:	0f b6 d0             	movzx  edx,al
    1539:	0f b6 45 fc          	movzx  eax,BYTE PTR [rbp-0x4]
    153d:	c0 f8 04             	sar    al,0x4
    1540:	0f be c0             	movsx  eax,al
    1543:	01 d0                	add    eax,edx
    1545:	3d 97 00 00 00       	cmp    eax,0x97
    154a:	0f 94 c0             	sete   al
    154d:	5d                   	pop    rbp
    154e:	c3                   	ret    

000000000000154f <f684565>:
    154f:	f3 0f 1e fa          	endbr64 
    1553:	55                   	push   rbp
    1554:	48 89 e5             	mov    rbp,rsp
    1557:	89 f8                	mov    eax,edi
    1559:	88 45 fc             	mov    BYTE PTR [rbp-0x4],al
    155c:	0f be 45 fc          	movsx  eax,BYTE PTR [rbp-0x4]
    1560:	c1 e0 04             	shl    eax,0x4
    1563:	0f b6 d0             	movzx  edx,al
    1566:	0f b6 45 fc          	movzx  eax,BYTE PTR [rbp-0x4]
    156a:	c0 f8 04             	sar    al,0x4
    156d:	0f be c0             	movsx  eax,al
    1570:	01 d0                	add    eax,edx
    1572:	3d f5 00 00 00       	cmp    eax,0xf5
    1577:	0f 94 c0             	sete   al
    157a:	5d                   	pop    rbp
    157b:	c3                   	ret    

000000000000157c <f92520>:
    157c:	f3 0f 1e fa          	endbr64 
    1580:	55                   	push   rbp
    1581:	48 89 e5             	mov    rbp,rsp
    1584:	89 f8                	mov    eax,edi
    1586:	88 45 fc             	mov    BYTE PTR [rbp-0x4],al
    1589:	0f be 45 fc          	movsx  eax,BYTE PTR [rbp-0x4]
    158d:	c1 e0 04             	shl    eax,0x4
    1590:	0f b6 d0             	movzx  edx,al
    1593:	0f b6 45 fc          	movzx  eax,BYTE PTR [rbp-0x4]
    1597:	c0 f8 04             	sar    al,0x4
    159a:	0f be c0             	movsx  eax,al
    159d:	01 d0                	add    eax,edx
    159f:	83 f8 47             	cmp    eax,0x47
    15a2:	0f 94 c0             	sete   al
    15a5:	5d                   	pop    rbp
    15a6:	c3                   	ret    

00000000000015a7 <f2033367>:
    15a7:	f3 0f 1e fa          	endbr64 
    15ab:	55                   	push   rbp
    15ac:	48 89 e5             	mov    rbp,rsp
    15af:	89 f8                	mov    eax,edi
    15b1:	88 45 fc             	mov    BYTE PTR [rbp-0x4],al
    15b4:	0f be 45 fc          	movsx  eax,BYTE PTR [rbp-0x4]
    15b8:	c1 e0 04             	shl    eax,0x4
    15bb:	0f b6 d0             	movzx  edx,al
    15be:	0f b6 45 fc          	movzx  eax,BYTE PTR [rbp-0x4]
    15c2:	c0 f8 04             	sar    al,0x4
    15c5:	0f be c0             	movsx  eax,al
    15c8:	01 d0                	add    eax,edx
    15ca:	3d 86 00 00 00       	cmp    eax,0x86
    15cf:	0f 94 c0             	sete   al
    15d2:	5d                   	pop    rbp
    15d3:	c3                   	ret    

00000000000015d4 <f554708>:
    15d4:	f3 0f 1e fa          	endbr64 
    15d8:	55                   	push   rbp
    15d9:	48 89 e5             	mov    rbp,rsp
    15dc:	89 f8                	mov    eax,edi
    15de:	88 45 fc             	mov    BYTE PTR [rbp-0x4],al
    15e1:	0f be 45 fc          	movsx  eax,BYTE PTR [rbp-0x4]
    15e5:	c1 e0 04             	shl    eax,0x4
    15e8:	0f b6 d0             	movzx  edx,al
    15eb:	0f b6 45 fc          	movzx  eax,BYTE PTR [rbp-0x4]
    15ef:	c0 f8 04             	sar    al,0x4
    15f2:	0f be c0             	movsx  eax,al
    15f5:	01 d0                	add    eax,edx
    15f7:	83 f8 13             	cmp    eax,0x13
    15fa:	0f 94 c0             	sete   al
    15fd:	5d                   	pop    rbp
    15fe:	c3                   	ret    

00000000000015ff <f5673323>:
    15ff:	f3 0f 1e fa          	endbr64 
    1603:	55                   	push   rbp
    1604:	48 89 e5             	mov    rbp,rsp
    1607:	89 f8                	mov    eax,edi
    1609:	88 45 fc             	mov    BYTE PTR [rbp-0x4],al
    160c:	0f be 45 fc          	movsx  eax,BYTE PTR [rbp-0x4]
    1610:	c1 e0 04             	shl    eax,0x4
    1613:	0f b6 d0             	movzx  edx,al
    1616:	0f b6 45 fc          	movzx  eax,BYTE PTR [rbp-0x4]
    161a:	c0 f8 04             	sar    al,0x4
    161d:	0f be c0             	movsx  eax,al
    1620:	01 d0                	add    eax,edx
    1622:	3d e6 00 00 00       	cmp    eax,0xe6
    1627:	0f 94 c0             	sete   al
    162a:	5d                   	pop    rbp
    162b:	c3                   	ret    

000000000000162c <f4231114>:
    162c:	f3 0f 1e fa          	endbr64 
    1630:	55                   	push   rbp
    1631:	48 89 e5             	mov    rbp,rsp
    1634:	89 f8                	mov    eax,edi
    1636:	88 45 fc             	mov    BYTE PTR [rbp-0x4],al
    1639:	0f be 45 fc          	movsx  eax,BYTE PTR [rbp-0x4]
    163d:	c1 e0 04             	shl    eax,0x4
    1640:	0f b6 d0             	movzx  edx,al
    1643:	0f b6 45 fc          	movzx  eax,BYTE PTR [rbp-0x4]
    1647:	c0 f8 04             	sar    al,0x4
    164a:	0f be c0             	movsx  eax,al
    164d:	01 d0                	add    eax,edx
    164f:	3d b6 00 00 00       	cmp    eax,0xb6
    1654:	0f 94 c0             	sete   al
    1657:	5d                   	pop    rbp
    1658:	c3                   	ret    

0000000000001659 <f7418636>:
    1659:	f3 0f 1e fa          	endbr64 
    165d:	55                   	push   rbp
    165e:	48 89 e5             	mov    rbp,rsp
    1661:	89 f8                	mov    eax,edi
    1663:	88 45 fc             	mov    BYTE PTR [rbp-0x4],al
    1666:	0f be 45 fc          	movsx  eax,BYTE PTR [rbp-0x4]
    166a:	c1 e0 04             	shl    eax,0x4
    166d:	0f b6 d0             	movzx  edx,al
    1670:	0f b6 45 fc          	movzx  eax,BYTE PTR [rbp-0x4]
    1674:	c0 f8 04             	sar    al,0x4
    1677:	0f be c0             	movsx  eax,al
    167a:	01 d0                	add    eax,edx
    167c:	83 f8 13             	cmp    eax,0x13
    167f:	0f 94 c0             	sete   al
    1682:	5d                   	pop    rbp
    1683:	c3                   	ret    

0000000000001684 <f1853358>:
    1684:	f3 0f 1e fa          	endbr64 
    1688:	55                   	push   rbp
    1689:	48 89 e5             	mov    rbp,rsp
    168c:	89 f8                	mov    eax,edi
    168e:	88 45 fc             	mov    BYTE PTR [rbp-0x4],al
    1691:	0f be 45 fc          	movsx  eax,BYTE PTR [rbp-0x4]
    1695:	c1 e0 04             	shl    eax,0x4
    1698:	0f b6 d0             	movzx  edx,al
    169b:	0f b6 45 fc          	movzx  eax,BYTE PTR [rbp-0x4]
    169f:	c0 f8 04             	sar    al,0x4
    16a2:	0f be c0             	movsx  eax,al
    16a5:	01 d0                	add    eax,edx
    16a7:	3d e6 00 00 00       	cmp    eax,0xe6
    16ac:	0f 94 c0             	sete   al
    16af:	5d                   	pop    rbp
    16b0:	c3                   	ret    

00000000000016b1 <f1991208>:
    16b1:	f3 0f 1e fa          	endbr64 
    16b5:	55                   	push   rbp
    16b6:	48 89 e5             	mov    rbp,rsp
    16b9:	89 f8                	mov    eax,edi
    16bb:	88 45 fc             	mov    BYTE PTR [rbp-0x4],al
    16be:	0f be 45 fc          	movsx  eax,BYTE PTR [rbp-0x4]
    16c2:	c1 e0 04             	shl    eax,0x4
    16c5:	0f b6 d0             	movzx  edx,al
    16c8:	0f b6 45 fc          	movzx  eax,BYTE PTR [rbp-0x4]
    16cc:	c0 f8 04             	sar    al,0x4
    16cf:	0f be c0             	movsx  eax,al
    16d2:	01 d0                	add    eax,edx
    16d4:	3d 93 00 00 00       	cmp    eax,0x93
    16d9:	0f 94 c0             	sete   al
    16dc:	5d                   	pop    rbp
    16dd:	c3                   	ret    

00000000000016de <f6976528>:
    16de:	f3 0f 1e fa          	endbr64 
    16e2:	55                   	push   rbp
    16e3:	48 89 e5             	mov    rbp,rsp
    16e6:	89 f8                	mov    eax,edi
    16e8:	88 45 fc             	mov    BYTE PTR [rbp-0x4],al
    16eb:	0f be 45 fc          	movsx  eax,BYTE PTR [rbp-0x4]
    16ef:	c1 e0 04             	shl    eax,0x4
    16f2:	0f b6 d0             	movzx  edx,al
    16f5:	0f b6 45 fc          	movzx  eax,BYTE PTR [rbp-0x4]
    16f9:	c0 f8 04             	sar    al,0x4
    16fc:	0f be c0             	movsx  eax,al
    16ff:	01 d0                	add    eax,edx
    1701:	3d f5 00 00 00       	cmp    eax,0xf5
    1706:	0f 94 c0             	sete   al
    1709:	5d                   	pop    rbp
    170a:	c3                   	ret    

000000000000170b <f3698419>:
    170b:	f3 0f 1e fa          	endbr64 
    170f:	55                   	push   rbp
    1710:	48 89 e5             	mov    rbp,rsp
    1713:	89 f8                	mov    eax,edi
    1715:	88 45 fc             	mov    BYTE PTR [rbp-0x4],al
    1718:	0f be 45 fc          	movsx  eax,BYTE PTR [rbp-0x4]
    171c:	c1 e0 04             	shl    eax,0x4
    171f:	0f b6 d0             	movzx  edx,al
    1722:	0f b6 45 fc          	movzx  eax,BYTE PTR [rbp-0x4]
    1726:	c0 f8 04             	sar    al,0x4
    1729:	0f be c0             	movsx  eax,al
    172c:	01 d0                	add    eax,edx
    172e:	83 f8 47             	cmp    eax,0x47
    1731:	0f 94 c0             	sete   al
    1734:	5d                   	pop    rbp
    1735:	c3                   	ret    

0000000000001736 <f2566491>:
    1736:	f3 0f 1e fa          	endbr64 
    173a:	55                   	push   rbp
    173b:	48 89 e5             	mov    rbp,rsp
    173e:	89 f8                	mov    eax,edi
    1740:	88 45 fc             	mov    BYTE PTR [rbp-0x4],al
    1743:	0f be 45 fc          	movsx  eax,BYTE PTR [rbp-0x4]
    1747:	c1 e0 04             	shl    eax,0x4
    174a:	0f b6 d0             	movzx  edx,al
    174d:	0f b6 45 fc          	movzx  eax,BYTE PTR [rbp-0x4]
    1751:	c0 f8 04             	sar    al,0x4
    1754:	0f be c0             	movsx  eax,al
    1757:	01 d0                	add    eax,edx
    1759:	3d 86 00 00 00       	cmp    eax,0x86
    175e:	0f 94 c0             	sete   al
    1761:	5d                   	pop    rbp
    1762:	c3                   	ret    

0000000000001763 <f7994952>:
    1763:	f3 0f 1e fa          	endbr64 
    1767:	55                   	push   rbp
    1768:	48 89 e5             	mov    rbp,rsp
    176b:	89 f8                	mov    eax,edi
    176d:	88 45 fc             	mov    BYTE PTR [rbp-0x4],al
    1770:	0f be 45 fc          	movsx  eax,BYTE PTR [rbp-0x4]
    1774:	c1 e0 04             	shl    eax,0x4
    1777:	0f b6 d0             	movzx  edx,al
    177a:	0f b6 45 fc          	movzx  eax,BYTE PTR [rbp-0x4]
    177e:	c0 f8 04             	sar    al,0x4
    1781:	0f be c0             	movsx  eax,al
    1784:	01 d0                	add    eax,edx
    1786:	83 f8 43             	cmp    eax,0x43
    1789:	0f 94 c0             	sete   al
    178c:	5d                   	pop    rbp
    178d:	c3                   	ret    

000000000000178e <f5140713>:
    178e:	f3 0f 1e fa          	endbr64 
    1792:	55                   	push   rbp
    1793:	48 89 e5             	mov    rbp,rsp
    1796:	89 f8                	mov    eax,edi
    1798:	88 45 fc             	mov    BYTE PTR [rbp-0x4],al
    179b:	0f be 45 fc          	movsx  eax,BYTE PTR [rbp-0x4]
    179f:	c1 e0 04             	shl    eax,0x4
    17a2:	0f b6 d0             	movzx  edx,al
    17a5:	0f b6 45 fc          	movzx  eax,BYTE PTR [rbp-0x4]
    17a9:	c0 f8 04             	sar    al,0x4
    17ac:	0f be c0             	movsx  eax,al
    17af:	01 d0                	add    eax,edx
    17b1:	83 f8 47             	cmp    eax,0x47
    17b4:	0f 94 c0             	sete   al
    17b7:	5d                   	pop    rbp
    17b8:	c3                   	ret    

00000000000017b9 <f88780>:
    17b9:	f3 0f 1e fa          	endbr64 
    17bd:	55                   	push   rbp
    17be:	48 89 e5             	mov    rbp,rsp
    17c1:	89 f8                	mov    eax,edi
    17c3:	88 45 fc             	mov    BYTE PTR [rbp-0x4],al
    17c6:	0f be 45 fc          	movsx  eax,BYTE PTR [rbp-0x4]
    17ca:	c1 e0 04             	shl    eax,0x4
    17cd:	0f b6 d0             	movzx  edx,al
    17d0:	0f b6 45 fc          	movzx  eax,BYTE PTR [rbp-0x4]
    17d4:	c0 f8 04             	sar    al,0x4
    17d7:	0f be c0             	movsx  eax,al
    17da:	01 d0                	add    eax,edx
    17dc:	3d f5 00 00 00       	cmp    eax,0xf5
    17e1:	0f 94 c0             	sete   al
    17e4:	5d                   	pop    rbp
    17e5:	c3                   	ret    

00000000000017e6 <f2161814>:
    17e6:	f3 0f 1e fa          	endbr64 
    17ea:	55                   	push   rbp
    17eb:	48 89 e5             	mov    rbp,rsp
    17ee:	89 f8                	mov    eax,edi
    17f0:	88 45 fc             	mov    BYTE PTR [rbp-0x4],al
    17f3:	0f be 45 fc          	movsx  eax,BYTE PTR [rbp-0x4]
    17f7:	c1 e0 04             	shl    eax,0x4
    17fa:	0f b6 d0             	movzx  edx,al
    17fd:	0f b6 45 fc          	movzx  eax,BYTE PTR [rbp-0x4]
    1801:	c0 f8 04             	sar    al,0x4
    1804:	0f be c0             	movsx  eax,al
    1807:	01 d0                	add    eax,edx
    1809:	3d 97 00 00 00       	cmp    eax,0x97
    180e:	0f 94 c0             	sete   al
    1811:	5d                   	pop    rbp
    1812:	c3                   	ret    

0000000000001813 <f9633522>:
    1813:	f3 0f 1e fa          	endbr64 
    1817:	55                   	push   rbp
    1818:	48 89 e5             	mov    rbp,rsp
    181b:	89 f8                	mov    eax,edi
    181d:	88 45 fc             	mov    BYTE PTR [rbp-0x4],al
    1820:	0f be 45 fc          	movsx  eax,BYTE PTR [rbp-0x4]
    1824:	c1 e0 04             	shl    eax,0x4
    1827:	0f b6 d0             	movzx  edx,al
    182a:	0f b6 45 fc          	movzx  eax,BYTE PTR [rbp-0x4]
    182e:	c0 f8 04             	sar    al,0x4
    1831:	0f be c0             	movsx  eax,al
    1834:	01 d0                	add    eax,edx
    1836:	83 f8 03             	cmp    eax,0x3
    1839:	0f 94 c0             	sete   al
    183c:	5d                   	pop    rbp
    183d:	c3                   	ret    

000000000000183e <f4283702>:
    183e:	f3 0f 1e fa          	endbr64 
    1842:	55                   	push   rbp
    1843:	48 89 e5             	mov    rbp,rsp
    1846:	89 f8                	mov    eax,edi
    1848:	88 45 fc             	mov    BYTE PTR [rbp-0x4],al
    184b:	0f be 45 fc          	movsx  eax,BYTE PTR [rbp-0x4]
    184f:	c1 e0 04             	shl    eax,0x4
    1852:	0f b6 d0             	movzx  edx,al
    1855:	0f b6 45 fc          	movzx  eax,BYTE PTR [rbp-0x4]
    1859:	c0 f8 04             	sar    al,0x4
    185c:	0f be c0             	movsx  eax,al
    185f:	01 d0                	add    eax,edx
    1861:	83 f8 57             	cmp    eax,0x57
    1864:	0f 94 c0             	sete   al
    1867:	5d                   	pop    rbp
    1868:	c3                   	ret    

0000000000001869 <f4865077>:
    1869:	f3 0f 1e fa          	endbr64 
    186d:	55                   	push   rbp
    186e:	48 89 e5             	mov    rbp,rsp
    1871:	89 f8                	mov    eax,edi
    1873:	88 45 fc             	mov    BYTE PTR [rbp-0x4],al
    1876:	0f be 45 fc          	movsx  eax,BYTE PTR [rbp-0x4]
    187a:	c1 e0 04             	shl    eax,0x4
    187d:	0f b6 d0             	movzx  edx,al
    1880:	0f b6 45 fc          	movzx  eax,BYTE PTR [rbp-0x4]
    1884:	c0 f8 04             	sar    al,0x4
    1887:	0f be c0             	movsx  eax,al
    188a:	01 d0                	add    eax,edx
    188c:	3d f5 00 00 00       	cmp    eax,0xf5
    1891:	0f 94 c0             	sete   al
    1894:	5d                   	pop    rbp
    1895:	c3                   	ret    

0000000000001896 <f5077469>:
    1896:	f3 0f 1e fa          	endbr64 
    189a:	55                   	push   rbp
    189b:	48 89 e5             	mov    rbp,rsp
    189e:	89 f8                	mov    eax,edi
    18a0:	88 45 fc             	mov    BYTE PTR [rbp-0x4],al
    18a3:	0f be 45 fc          	movsx  eax,BYTE PTR [rbp-0x4]
    18a7:	c1 e0 04             	shl    eax,0x4
    18aa:	0f b6 d0             	movzx  edx,al
    18ad:	0f b6 45 fc          	movzx  eax,BYTE PTR [rbp-0x4]
    18b1:	c0 f8 04             	sar    al,0x4
    18b4:	0f be c0             	movsx  eax,al
    18b7:	01 d0                	add    eax,edx
    18b9:	83 f8 36             	cmp    eax,0x36
    18bc:	0f 94 c0             	sete   al
    18bf:	5d                   	pop    rbp
    18c0:	c3                   	ret    

00000000000018c1 <f8942470>:
    18c1:	f3 0f 1e fa          	endbr64 
    18c5:	55                   	push   rbp
    18c6:	48 89 e5             	mov    rbp,rsp
    18c9:	89 f8                	mov    eax,edi
    18cb:	88 45 fc             	mov    BYTE PTR [rbp-0x4],al
    18ce:	0f be 45 fc          	movsx  eax,BYTE PTR [rbp-0x4]
    18d2:	c1 e0 04             	shl    eax,0x4
    18d5:	0f b6 d0             	movzx  edx,al
    18d8:	0f b6 45 fc          	movzx  eax,BYTE PTR [rbp-0x4]
    18dc:	c0 f8 04             	sar    al,0x4
    18df:	0f be c0             	movsx  eax,al
    18e2:	01 d0                	add    eax,edx
    18e4:	83 f8 43             	cmp    eax,0x43
    18e7:	0f 94 c0             	sete   al
    18ea:	5d                   	pop    rbp
    18eb:	c3                   	ret    

00000000000018ec <f69599>:
    18ec:	f3 0f 1e fa          	endbr64 
    18f0:	55                   	push   rbp
    18f1:	48 89 e5             	mov    rbp,rsp
    18f4:	89 f8                	mov    eax,edi
    18f6:	88 45 fc             	mov    BYTE PTR [rbp-0x4],al
    18f9:	0f be 45 fc          	movsx  eax,BYTE PTR [rbp-0x4]
    18fd:	c1 e0 04             	shl    eax,0x4
    1900:	0f b6 d0             	movzx  edx,al
    1903:	0f b6 45 fc          	movzx  eax,BYTE PTR [rbp-0x4]
    1907:	c0 f8 04             	sar    al,0x4
    190a:	0f be c0             	movsx  eax,al
    190d:	01 d0                	add    eax,edx
    190f:	3d e6 00 00 00       	cmp    eax,0xe6
    1914:	0f 94 c0             	sete   al
    1917:	5d                   	pop    rbp
    1918:	c3                   	ret    

0000000000001919 <f306115>:
    1919:	f3 0f 1e fa          	endbr64 
    191d:	55                   	push   rbp
    191e:	48 89 e5             	mov    rbp,rsp
    1921:	89 f8                	mov    eax,edi
    1923:	88 45 fc             	mov    BYTE PTR [rbp-0x4],al
    1926:	0f be 45 fc          	movsx  eax,BYTE PTR [rbp-0x4]
    192a:	c1 e0 04             	shl    eax,0x4
    192d:	0f b6 d0             	movzx  edx,al
    1930:	0f b6 45 fc          	movzx  eax,BYTE PTR [rbp-0x4]
    1934:	c0 f8 04             	sar    al,0x4
    1937:	0f be c0             	movsx  eax,al
    193a:	01 d0                	add    eax,edx
    193c:	3d f5 00 00 00       	cmp    eax,0xf5
    1941:	0f 94 c0             	sete   al
    1944:	5d                   	pop    rbp
    1945:	c3                   	ret    

0000000000001946 <f5819085>:
    1946:	f3 0f 1e fa          	endbr64 
    194a:	55                   	push   rbp
    194b:	48 89 e5             	mov    rbp,rsp
    194e:	89 f8                	mov    eax,edi
    1950:	88 45 fc             	mov    BYTE PTR [rbp-0x4],al
    1953:	0f be 45 fc          	movsx  eax,BYTE PTR [rbp-0x4]
    1957:	c1 e0 04             	shl    eax,0x4
    195a:	0f b6 d0             	movzx  edx,al
    195d:	0f b6 45 fc          	movzx  eax,BYTE PTR [rbp-0x4]
    1961:	c0 f8 04             	sar    al,0x4
    1964:	0f be c0             	movsx  eax,al
    1967:	01 d0                	add    eax,edx
    1969:	83 f8 47             	cmp    eax,0x47
    196c:	0f 94 c0             	sete   al
    196f:	5d                   	pop    rbp
    1970:	c3                   	ret    

0000000000001971 <f2051229>:
    1971:	f3 0f 1e fa          	endbr64 
    1975:	55                   	push   rbp
    1976:	48 89 e5             	mov    rbp,rsp
    1979:	89 f8                	mov    eax,edi
    197b:	88 45 fc             	mov    BYTE PTR [rbp-0x4],al
    197e:	0f be 45 fc          	movsx  eax,BYTE PTR [rbp-0x4]
    1982:	c1 e0 04             	shl    eax,0x4
    1985:	0f b6 d0             	movzx  edx,al
    1988:	0f b6 45 fc          	movzx  eax,BYTE PTR [rbp-0x4]
    198c:	c0 f8 04             	sar    al,0x4
    198f:	0f be c0             	movsx  eax,al
    1992:	01 d0                	add    eax,edx
    1994:	83 f8 27             	cmp    eax,0x27
    1997:	0f 94 c0             	sete   al
    199a:	5d                   	pop    rbp
    199b:	c3                   	ret    

000000000000199c <f8121604>:
    199c:	f3 0f 1e fa          	endbr64 
    19a0:	55                   	push   rbp
    19a1:	48 89 e5             	mov    rbp,rsp
    19a4:	89 f8                	mov    eax,edi
    19a6:	88 45 fc             	mov    BYTE PTR [rbp-0x4],al
    19a9:	0f be 45 fc          	movsx  eax,BYTE PTR [rbp-0x4]
    19ad:	c1 e0 04             	shl    eax,0x4
    19b0:	0f b6 d0             	movzx  edx,al
    19b3:	0f b6 45 fc          	movzx  eax,BYTE PTR [rbp-0x4]
    19b7:	c0 f8 04             	sar    al,0x4
    19ba:	0f be c0             	movsx  eax,al
    19bd:	01 d0                	add    eax,edx
    19bf:	3d 97 00 00 00       	cmp    eax,0x97
    19c4:	0f 94 c0             	sete   al
    19c7:	5d                   	pop    rbp
    19c8:	c3                   	ret    

00000000000019c9 <f5595266>:
    19c9:	f3 0f 1e fa          	endbr64 
    19cd:	55                   	push   rbp
    19ce:	48 89 e5             	mov    rbp,rsp
    19d1:	89 f8                	mov    eax,edi
    19d3:	88 45 fc             	mov    BYTE PTR [rbp-0x4],al
    19d6:	0f be 45 fc          	movsx  eax,BYTE PTR [rbp-0x4]
    19da:	c1 e0 04             	shl    eax,0x4
    19dd:	0f b6 d0             	movzx  edx,al
    19e0:	0f b6 45 fc          	movzx  eax,BYTE PTR [rbp-0x4]
    19e4:	c0 f8 04             	sar    al,0x4
    19e7:	0f be c0             	movsx  eax,al
    19ea:	01 d0                	add    eax,edx
    19ec:	3d f5 00 00 00       	cmp    eax,0xf5
    19f1:	0f 94 c0             	sete   al
    19f4:	5d                   	pop    rbp
    19f5:	c3                   	ret    

00000000000019f6 <f3404320>:
    19f6:	f3 0f 1e fa          	endbr64 
    19fa:	55                   	push   rbp
    19fb:	48 89 e5             	mov    rbp,rsp
    19fe:	89 f8                	mov    eax,edi
    1a00:	88 45 fc             	mov    BYTE PTR [rbp-0x4],al
    1a03:	0f be 45 fc          	movsx  eax,BYTE PTR [rbp-0x4]
    1a07:	c1 e0 04             	shl    eax,0x4
    1a0a:	0f b6 d0             	movzx  edx,al
    1a0d:	0f b6 45 fc          	movzx  eax,BYTE PTR [rbp-0x4]
    1a11:	c0 f8 04             	sar    al,0x4
    1a14:	0f be c0             	movsx  eax,al
    1a17:	01 d0                	add    eax,edx
    1a19:	83 f8 47             	cmp    eax,0x47
    1a1c:	0f 94 c0             	sete   al
    1a1f:	5d                   	pop    rbp
    1a20:	c3                   	ret    

0000000000001a21 <f4356041>:
    1a21:	f3 0f 1e fa          	endbr64 
    1a25:	55                   	push   rbp
    1a26:	48 89 e5             	mov    rbp,rsp
    1a29:	89 f8                	mov    eax,edi
    1a2b:	88 45 fc             	mov    BYTE PTR [rbp-0x4],al
    1a2e:	0f be 45 fc          	movsx  eax,BYTE PTR [rbp-0x4]
    1a32:	c1 e0 04             	shl    eax,0x4
    1a35:	0f b6 d0             	movzx  edx,al
    1a38:	0f b6 45 fc          	movzx  eax,BYTE PTR [rbp-0x4]
    1a3c:	c0 f8 04             	sar    al,0x4
    1a3f:	0f be c0             	movsx  eax,al
    1a42:	01 d0                	add    eax,edx
    1a44:	3d 86 00 00 00       	cmp    eax,0x86
    1a49:	0f 94 c0             	sete   al
    1a4c:	5d                   	pop    rbp
    1a4d:	c3                   	ret    

0000000000001a4e <f3676482>:
    1a4e:	f3 0f 1e fa          	endbr64 
    1a52:	55                   	push   rbp
    1a53:	48 89 e5             	mov    rbp,rsp
    1a56:	89 f8                	mov    eax,edi
    1a58:	88 45 fc             	mov    BYTE PTR [rbp-0x4],al
    1a5b:	0f be 45 fc          	movsx  eax,BYTE PTR [rbp-0x4]
    1a5f:	c1 e0 04             	shl    eax,0x4
    1a62:	0f b6 d0             	movzx  edx,al
    1a65:	0f b6 45 fc          	movzx  eax,BYTE PTR [rbp-0x4]
    1a69:	c0 f8 04             	sar    al,0x4
    1a6c:	0f be c0             	movsx  eax,al
    1a6f:	01 d0                	add    eax,edx
    1a71:	83 f8 13             	cmp    eax,0x13
    1a74:	0f 94 c0             	sete   al
    1a77:	5d                   	pop    rbp
    1a78:	c3                   	ret    

0000000000001a79 <f285854>:
    1a79:	f3 0f 1e fa          	endbr64 
    1a7d:	55                   	push   rbp
    1a7e:	48 89 e5             	mov    rbp,rsp
    1a81:	89 f8                	mov    eax,edi
    1a83:	88 45 fc             	mov    BYTE PTR [rbp-0x4],al
    1a86:	0f be 45 fc          	movsx  eax,BYTE PTR [rbp-0x4]
    1a8a:	c1 e0 04             	shl    eax,0x4
    1a8d:	0f b6 d0             	movzx  edx,al
    1a90:	0f b6 45 fc          	movzx  eax,BYTE PTR [rbp-0x4]
    1a94:	c0 f8 04             	sar    al,0x4
    1a97:	0f be c0             	movsx  eax,al
    1a9a:	01 d0                	add    eax,edx
    1a9c:	83 f8 53             	cmp    eax,0x53
    1a9f:	0f 94 c0             	sete   al
    1aa2:	5d                   	pop    rbp
    1aa3:	c3                   	ret    

0000000000001aa4 <f4534378>:
    1aa4:	f3 0f 1e fa          	endbr64 
    1aa8:	55                   	push   rbp
    1aa9:	48 89 e5             	mov    rbp,rsp
    1aac:	89 f8                	mov    eax,edi
    1aae:	88 45 fc             	mov    BYTE PTR [rbp-0x4],al
    1ab1:	0f be 45 fc          	movsx  eax,BYTE PTR [rbp-0x4]
    1ab5:	c1 e0 04             	shl    eax,0x4
    1ab8:	0f b6 d0             	movzx  edx,al
    1abb:	0f b6 45 fc          	movzx  eax,BYTE PTR [rbp-0x4]
    1abf:	c0 f8 04             	sar    al,0x4
    1ac2:	0f be c0             	movsx  eax,al
    1ac5:	01 d0                	add    eax,edx
    1ac7:	3d f5 00 00 00       	cmp    eax,0xf5
    1acc:	0f 94 c0             	sete   al
    1acf:	5d                   	pop    rbp
    1ad0:	c3                   	ret    

0000000000001ad1 <f5431748>:
    1ad1:	f3 0f 1e fa          	endbr64 
    1ad5:	55                   	push   rbp
    1ad6:	48 89 e5             	mov    rbp,rsp
    1ad9:	89 f8                	mov    eax,edi
    1adb:	88 45 fc             	mov    BYTE PTR [rbp-0x4],al
    1ade:	0f be 45 fc          	movsx  eax,BYTE PTR [rbp-0x4]
    1ae2:	c1 e0 04             	shl    eax,0x4
    1ae5:	0f b6 d0             	movzx  edx,al
    1ae8:	0f b6 45 fc          	movzx  eax,BYTE PTR [rbp-0x4]
    1aec:	c0 f8 04             	sar    al,0x4
    1aef:	0f be c0             	movsx  eax,al
    1af2:	01 d0                	add    eax,edx
    1af4:	3d d6 00 00 00       	cmp    eax,0xd6
    1af9:	0f 94 c0             	sete   al
    1afc:	5d                   	pop    rbp
    1afd:	c3                   	ret    

0000000000001afe <f3034080>:
    1afe:	f3 0f 1e fa          	endbr64 
    1b02:	55                   	push   rbp
    1b03:	48 89 e5             	mov    rbp,rsp
    1b06:	89 f8                	mov    eax,edi
    1b08:	88 45 fc             	mov    BYTE PTR [rbp-0x4],al
    1b0b:	0f be 45 fc          	movsx  eax,BYTE PTR [rbp-0x4]
    1b0f:	c1 e0 04             	shl    eax,0x4
    1b12:	0f b6 d0             	movzx  edx,al
    1b15:	0f b6 45 fc          	movzx  eax,BYTE PTR [rbp-0x4]
    1b19:	c0 f8 04             	sar    al,0x4
    1b1c:	0f be c0             	movsx  eax,al
    1b1f:	01 d0                	add    eax,edx
    1b21:	83 f8 43             	cmp    eax,0x43
    1b24:	0f 94 c0             	sete   al
    1b27:	5d                   	pop    rbp
    1b28:	c3                   	ret    

0000000000001b29 <f6793597>:
    1b29:	f3 0f 1e fa          	endbr64 
    1b2d:	55                   	push   rbp
    1b2e:	48 89 e5             	mov    rbp,rsp
    1b31:	89 f8                	mov    eax,edi
    1b33:	88 45 fc             	mov    BYTE PTR [rbp-0x4],al
    1b36:	0f be 45 fc          	movsx  eax,BYTE PTR [rbp-0x4]
    1b3a:	c1 e0 04             	shl    eax,0x4
    1b3d:	0f b6 d0             	movzx  edx,al
    1b40:	0f b6 45 fc          	movzx  eax,BYTE PTR [rbp-0x4]
    1b44:	c0 f8 04             	sar    al,0x4
    1b47:	0f be c0             	movsx  eax,al
    1b4a:	01 d0                	add    eax,edx
    1b4c:	3d e6 00 00 00       	cmp    eax,0xe6
    1b51:	0f 94 c0             	sete   al
    1b54:	5d                   	pop    rbp
    1b55:	c3                   	ret    

0000000000001b56 <f2069805>:
    1b56:	f3 0f 1e fa          	endbr64 
    1b5a:	55                   	push   rbp
    1b5b:	48 89 e5             	mov    rbp,rsp
    1b5e:	89 f8                	mov    eax,edi
    1b60:	88 45 fc             	mov    BYTE PTR [rbp-0x4],al
    1b63:	0f be 45 fc          	movsx  eax,BYTE PTR [rbp-0x4]
    1b67:	c1 e0 04             	shl    eax,0x4
    1b6a:	0f b6 d0             	movzx  edx,al
    1b6d:	0f b6 45 fc          	movzx  eax,BYTE PTR [rbp-0x4]
    1b71:	c0 f8 04             	sar    al,0x4
    1b74:	0f be c0             	movsx  eax,al
    1b77:	01 d0                	add    eax,edx
    1b79:	83 f8 57             	cmp    eax,0x57
    1b7c:	0f 94 c0             	sete   al
    1b7f:	5d                   	pop    rbp
    1b80:	c3                   	ret    

0000000000001b81 <f4427480>:
    1b81:	f3 0f 1e fa          	endbr64 
    1b85:	55                   	push   rbp
    1b86:	48 89 e5             	mov    rbp,rsp
    1b89:	89 f8                	mov    eax,edi
    1b8b:	88 45 fc             	mov    BYTE PTR [rbp-0x4],al
    1b8e:	0f be 45 fc          	movsx  eax,BYTE PTR [rbp-0x4]
    1b92:	c1 e0 04             	shl    eax,0x4
    1b95:	0f b6 d0             	movzx  edx,al
    1b98:	0f b6 45 fc          	movzx  eax,BYTE PTR [rbp-0x4]
    1b9c:	c0 f8 04             	sar    al,0x4
    1b9f:	0f be c0             	movsx  eax,al
    1ba2:	01 d0                	add    eax,edx
    1ba4:	83 f8 43             	cmp    eax,0x43
    1ba7:	0f 94 c0             	sete   al
    1baa:	5d                   	pop    rbp
    1bab:	c3                   	ret    

0000000000001bac <f6745606>:
    1bac:	f3 0f 1e fa          	endbr64 
    1bb0:	55                   	push   rbp
    1bb1:	48 89 e5             	mov    rbp,rsp
    1bb4:	89 f8                	mov    eax,edi
    1bb6:	88 45 fc             	mov    BYTE PTR [rbp-0x4],al
    1bb9:	0f be 45 fc          	movsx  eax,BYTE PTR [rbp-0x4]
    1bbd:	c1 e0 04             	shl    eax,0x4
    1bc0:	0f b6 d0             	movzx  edx,al
    1bc3:	0f b6 45 fc          	movzx  eax,BYTE PTR [rbp-0x4]
    1bc7:	c0 f8 04             	sar    al,0x4
    1bca:	0f be c0             	movsx  eax,al
    1bcd:	01 d0                	add    eax,edx
    1bcf:	3d c6 00 00 00       	cmp    eax,0xc6
    1bd4:	0f 94 c0             	sete   al
    1bd7:	5d                   	pop    rbp
    1bd8:	c3                   	ret    

0000000000001bd9 <f8019149>:
    1bd9:	f3 0f 1e fa          	endbr64 
    1bdd:	55                   	push   rbp
    1bde:	48 89 e5             	mov    rbp,rsp
    1be1:	89 f8                	mov    eax,edi
    1be3:	88 45 fc             	mov    BYTE PTR [rbp-0x4],al
    1be6:	0f be 45 fc          	movsx  eax,BYTE PTR [rbp-0x4]
    1bea:	c1 e0 04             	shl    eax,0x4
    1bed:	0f b6 d0             	movzx  edx,al
    1bf0:	0f b6 45 fc          	movzx  eax,BYTE PTR [rbp-0x4]
    1bf4:	c0 f8 04             	sar    al,0x4
    1bf7:	0f be c0             	movsx  eax,al
    1bfa:	01 d0                	add    eax,edx
    1bfc:	3d c6 00 00 00       	cmp    eax,0xc6
    1c01:	0f 94 c0             	sete   al
    1c04:	5d                   	pop    rbp
    1c05:	c3                   	ret    

0000000000001c06 <f5221954>:
    1c06:	f3 0f 1e fa          	endbr64 
    1c0a:	55                   	push   rbp
    1c0b:	48 89 e5             	mov    rbp,rsp
    1c0e:	89 f8                	mov    eax,edi
    1c10:	88 45 fc             	mov    BYTE PTR [rbp-0x4],al
    1c13:	0f be 45 fc          	movsx  eax,BYTE PTR [rbp-0x4]
    1c17:	c1 e0 04             	shl    eax,0x4
    1c1a:	0f b6 d0             	movzx  edx,al
    1c1d:	0f b6 45 fc          	movzx  eax,BYTE PTR [rbp-0x4]
    1c21:	c0 f8 04             	sar    al,0x4
    1c24:	0f be c0             	movsx  eax,al
    1c27:	01 d0                	add    eax,edx
    1c29:	3d 97 00 00 00       	cmp    eax,0x97
    1c2e:	0f 94 c0             	sete   al
    1c31:	5d                   	pop    rbp
    1c32:	c3                   	ret    

0000000000001c33 <f6822097>:
    1c33:	f3 0f 1e fa          	endbr64 
    1c37:	55                   	push   rbp
    1c38:	48 89 e5             	mov    rbp,rsp
    1c3b:	89 f8                	mov    eax,edi
    1c3d:	88 45 fc             	mov    BYTE PTR [rbp-0x4],al
    1c40:	0f be 45 fc          	movsx  eax,BYTE PTR [rbp-0x4]
    1c44:	c1 e0 04             	shl    eax,0x4
    1c47:	0f b6 d0             	movzx  edx,al
    1c4a:	0f b6 45 fc          	movzx  eax,BYTE PTR [rbp-0x4]
    1c4e:	c0 f8 04             	sar    al,0x4
    1c51:	0f be c0             	movsx  eax,al
    1c54:	01 d0                	add    eax,edx
    1c56:	3d f3 00 00 00       	cmp    eax,0xf3
    1c5b:	0f 94 c0             	sete   al
    1c5e:	5d                   	pop    rbp
    1c5f:	c3                   	ret    

0000000000001c60 <f9144894>:
    1c60:	f3 0f 1e fa          	endbr64 
    1c64:	55                   	push   rbp
    1c65:	48 89 e5             	mov    rbp,rsp
    1c68:	89 f8                	mov    eax,edi
    1c6a:	88 45 fc             	mov    BYTE PTR [rbp-0x4],al
    1c6d:	0f be 45 fc          	movsx  eax,BYTE PTR [rbp-0x4]
    1c71:	c1 e0 04             	shl    eax,0x4
    1c74:	0f b6 d0             	movzx  edx,al
    1c77:	0f b6 45 fc          	movzx  eax,BYTE PTR [rbp-0x4]
    1c7b:	c0 f8 04             	sar    al,0x4
    1c7e:	0f be c0             	movsx  eax,al
    1c81:	01 d0                	add    eax,edx
    1c83:	3d f3 00 00 00       	cmp    eax,0xf3
    1c88:	0f 94 c0             	sete   al
    1c8b:	5d                   	pop    rbp
    1c8c:	c3                   	ret    

0000000000001c8d <f9662054>:
    1c8d:	f3 0f 1e fa          	endbr64 
    1c91:	55                   	push   rbp
    1c92:	48 89 e5             	mov    rbp,rsp
    1c95:	89 f8                	mov    eax,edi
    1c97:	88 45 fc             	mov    BYTE PTR [rbp-0x4],al
    1c9a:	0f be 45 fc          	movsx  eax,BYTE PTR [rbp-0x4]
    1c9e:	c1 e0 04             	shl    eax,0x4
    1ca1:	0f b6 d0             	movzx  edx,al
    1ca4:	0f b6 45 fc          	movzx  eax,BYTE PTR [rbp-0x4]
    1ca8:	c0 f8 04             	sar    al,0x4
    1cab:	0f be c0             	movsx  eax,al
    1cae:	01 d0                	add    eax,edx
    1cb0:	3d f3 00 00 00       	cmp    eax,0xf3
    1cb5:	0f 94 c0             	sete   al
    1cb8:	5d                   	pop    rbp
    1cb9:	c3                   	ret    

0000000000001cba <f3474527>:
    1cba:	f3 0f 1e fa          	endbr64 
    1cbe:	55                   	push   rbp
    1cbf:	48 89 e5             	mov    rbp,rsp
    1cc2:	89 f8                	mov    eax,edi
    1cc4:	88 45 fc             	mov    BYTE PTR [rbp-0x4],al
    1cc7:	0f be 45 fc          	movsx  eax,BYTE PTR [rbp-0x4]
    1ccb:	c1 e0 04             	shl    eax,0x4
    1cce:	0f b6 d0             	movzx  edx,al
    1cd1:	0f b6 45 fc          	movzx  eax,BYTE PTR [rbp-0x4]
    1cd5:	c0 f8 04             	sar    al,0x4
    1cd8:	0f be c0             	movsx  eax,al
    1cdb:	01 d0                	add    eax,edx
    1cdd:	3d f5 00 00 00       	cmp    eax,0xf5
    1ce2:	0f 94 c0             	sete   al
    1ce5:	5d                   	pop    rbp
    1ce6:	c3                   	ret    

0000000000001ce7 <f543247>:
    1ce7:	f3 0f 1e fa          	endbr64 
    1ceb:	55                   	push   rbp
    1cec:	48 89 e5             	mov    rbp,rsp
    1cef:	89 f8                	mov    eax,edi
    1cf1:	88 45 fc             	mov    BYTE PTR [rbp-0x4],al
    1cf4:	0f be 45 fc          	movsx  eax,BYTE PTR [rbp-0x4]
    1cf8:	c1 e0 04             	shl    eax,0x4
    1cfb:	0f b6 d0             	movzx  edx,al
    1cfe:	0f b6 45 fc          	movzx  eax,BYTE PTR [rbp-0x4]
    1d02:	c0 f8 04             	sar    al,0x4
    1d05:	0f be c0             	movsx  eax,al
    1d08:	01 d0                	add    eax,edx
    1d0a:	3d f4 00 00 00       	cmp    eax,0xf4
    1d0f:	0f 94 c0             	sete   al
    1d12:	5d                   	pop    rbp
    1d13:	c3                   	ret    

0000000000001d14 <f7109986>:
    1d14:	f3 0f 1e fa          	endbr64 
    1d18:	55                   	push   rbp
    1d19:	48 89 e5             	mov    rbp,rsp
    1d1c:	89 f8                	mov    eax,edi
    1d1e:	88 45 fc             	mov    BYTE PTR [rbp-0x4],al
    1d21:	0f be 45 fc          	movsx  eax,BYTE PTR [rbp-0x4]
    1d25:	c1 e0 04             	shl    eax,0x4
    1d28:	0f b6 d0             	movzx  edx,al
    1d2b:	0f b6 45 fc          	movzx  eax,BYTE PTR [rbp-0x4]
    1d2f:	c0 f8 04             	sar    al,0x4
    1d32:	0f be c0             	movsx  eax,al
    1d35:	01 d0                	add    eax,edx
    1d37:	3d b6 00 00 00       	cmp    eax,0xb6
    1d3c:	0f 94 c0             	sete   al
    1d3f:	5d                   	pop    rbp
    1d40:	c3                   	ret    

0000000000001d41 <f6472803>:
    1d41:	f3 0f 1e fa          	endbr64 
    1d45:	55                   	push   rbp
    1d46:	48 89 e5             	mov    rbp,rsp
    1d49:	89 f8                	mov    eax,edi
    1d4b:	88 45 fc             	mov    BYTE PTR [rbp-0x4],al
    1d4e:	0f be 45 fc          	movsx  eax,BYTE PTR [rbp-0x4]
    1d52:	c1 e0 04             	shl    eax,0x4
    1d55:	0f b6 d0             	movzx  edx,al
    1d58:	0f b6 45 fc          	movzx  eax,BYTE PTR [rbp-0x4]
    1d5c:	c0 f8 04             	sar    al,0x4
    1d5f:	0f be c0             	movsx  eax,al
    1d62:	01 d0                	add    eax,edx
    1d64:	3d f5 00 00 00       	cmp    eax,0xf5
    1d69:	0f 94 c0             	sete   al
    1d6c:	5d                   	pop    rbp
    1d6d:	c3                   	ret    

0000000000001d6e <f7656586>:
    1d6e:	f3 0f 1e fa          	endbr64 
    1d72:	55                   	push   rbp
    1d73:	48 89 e5             	mov    rbp,rsp
    1d76:	89 f8                	mov    eax,edi
    1d78:	88 45 fc             	mov    BYTE PTR [rbp-0x4],al
    1d7b:	0f be 45 fc          	movsx  eax,BYTE PTR [rbp-0x4]
    1d7f:	c1 e0 04             	shl    eax,0x4
    1d82:	0f b6 d0             	movzx  edx,al
    1d85:	0f b6 45 fc          	movzx  eax,BYTE PTR [rbp-0x4]
    1d89:	c0 f8 04             	sar    al,0x4
    1d8c:	0f be c0             	movsx  eax,al
    1d8f:	01 d0                	add    eax,edx
    1d91:	3d 94 00 00 00       	cmp    eax,0x94
    1d96:	0f 94 c0             	sete   al
    1d99:	5d                   	pop    rbp
    1d9a:	c3                   	ret    

0000000000001d9b <f2884700>:
    1d9b:	f3 0f 1e fa          	endbr64 
    1d9f:	55                   	push   rbp
    1da0:	48 89 e5             	mov    rbp,rsp
    1da3:	89 f8                	mov    eax,edi
    1da5:	88 45 fc             	mov    BYTE PTR [rbp-0x4],al
    1da8:	0f be 45 fc          	movsx  eax,BYTE PTR [rbp-0x4]
    1dac:	c1 e0 04             	shl    eax,0x4
    1daf:	0f b6 d0             	movzx  edx,al
    1db2:	0f b6 45 fc          	movzx  eax,BYTE PTR [rbp-0x4]
    1db6:	c0 f8 04             	sar    al,0x4
    1db9:	0f be c0             	movsx  eax,al
    1dbc:	01 d0                	add    eax,edx
    1dbe:	3d f5 00 00 00       	cmp    eax,0xf5
    1dc3:	0f 94 c0             	sete   al
    1dc6:	5d                   	pop    rbp
    1dc7:	c3                   	ret    

0000000000001dc8 <f8976878>:
    1dc8:	f3 0f 1e fa          	endbr64 
    1dcc:	55                   	push   rbp
    1dcd:	48 89 e5             	mov    rbp,rsp
    1dd0:	89 f8                	mov    eax,edi
    1dd2:	88 45 fc             	mov    BYTE PTR [rbp-0x4],al
    1dd5:	0f be 45 fc          	movsx  eax,BYTE PTR [rbp-0x4]
    1dd9:	c1 e0 04             	shl    eax,0x4
    1ddc:	0f b6 d0             	movzx  edx,al
    1ddf:	0f b6 45 fc          	movzx  eax,BYTE PTR [rbp-0x4]
    1de3:	c0 f8 04             	sar    al,0x4
    1de6:	0f be c0             	movsx  eax,al
    1de9:	01 d0                	add    eax,edx
    1deb:	83 f8 47             	cmp    eax,0x47
    1dee:	0f 94 c0             	sete   al
    1df1:	5d                   	pop    rbp
    1df2:	c3                   	ret    

0000000000001df3 <f8152608>:
    1df3:	f3 0f 1e fa          	endbr64 
    1df7:	55                   	push   rbp
    1df8:	48 89 e5             	mov    rbp,rsp
    1dfb:	89 f8                	mov    eax,edi
    1dfd:	88 45 fc             	mov    BYTE PTR [rbp-0x4],al
    1e00:	0f be 45 fc          	movsx  eax,BYTE PTR [rbp-0x4]
    1e04:	c1 e0 04             	shl    eax,0x4
    1e07:	0f b6 d0             	movzx  edx,al
    1e0a:	0f b6 45 fc          	movzx  eax,BYTE PTR [rbp-0x4]
    1e0e:	c0 f8 04             	sar    al,0x4
    1e11:	0f be c0             	movsx  eax,al
    1e14:	01 d0                	add    eax,edx
    1e16:	3d 86 00 00 00       	cmp    eax,0x86
    1e1b:	0f 94 c0             	sete   al
    1e1e:	5d                   	pop    rbp
    1e1f:	c3                   	ret    

0000000000001e20 <f9818014>:
    1e20:	f3 0f 1e fa          	endbr64 
    1e24:	55                   	push   rbp
    1e25:	48 89 e5             	mov    rbp,rsp
    1e28:	89 f8                	mov    eax,edi
    1e2a:	88 45 fc             	mov    BYTE PTR [rbp-0x4],al
    1e2d:	0f be 45 fc          	movsx  eax,BYTE PTR [rbp-0x4]
    1e31:	c1 e0 04             	shl    eax,0x4
    1e34:	0f b6 d0             	movzx  edx,al
    1e37:	0f b6 45 fc          	movzx  eax,BYTE PTR [rbp-0x4]
    1e3b:	c0 f8 04             	sar    al,0x4
    1e3e:	0f be c0             	movsx  eax,al
    1e41:	01 d0                	add    eax,edx
    1e43:	83 f8 13             	cmp    eax,0x13
    1e46:	0f 94 c0             	sete   al
    1e49:	5d                   	pop    rbp
    1e4a:	c3                   	ret    

0000000000001e4b <f8511877>:
    1e4b:	f3 0f 1e fa          	endbr64 
    1e4f:	55                   	push   rbp
    1e50:	48 89 e5             	mov    rbp,rsp
    1e53:	89 f8                	mov    eax,edi
    1e55:	88 45 fc             	mov    BYTE PTR [rbp-0x4],al
    1e58:	0f be 45 fc          	movsx  eax,BYTE PTR [rbp-0x4]
    1e5c:	c1 e0 04             	shl    eax,0x4
    1e5f:	0f b6 d0             	movzx  edx,al
    1e62:	0f b6 45 fc          	movzx  eax,BYTE PTR [rbp-0x4]
    1e66:	c0 f8 04             	sar    al,0x4
    1e69:	0f be c0             	movsx  eax,al
    1e6c:	01 d0                	add    eax,edx
    1e6e:	3d e6 00 00 00       	cmp    eax,0xe6
    1e73:	0f 94 c0             	sete   al
    1e76:	5d                   	pop    rbp
    1e77:	c3                   	ret    

0000000000001e78 <f8107564>:
    1e78:	f3 0f 1e fa          	endbr64 
    1e7c:	55                   	push   rbp
    1e7d:	48 89 e5             	mov    rbp,rsp
    1e80:	89 f8                	mov    eax,edi
    1e82:	88 45 fc             	mov    BYTE PTR [rbp-0x4],al
    1e85:	0f be 45 fc          	movsx  eax,BYTE PTR [rbp-0x4]
    1e89:	c1 e0 04             	shl    eax,0x4
    1e8c:	0f b6 d0             	movzx  edx,al
    1e8f:	0f b6 45 fc          	movzx  eax,BYTE PTR [rbp-0x4]
    1e93:	c0 f8 04             	sar    al,0x4
    1e96:	0f be c0             	movsx  eax,al
    1e99:	01 d0                	add    eax,edx
    1e9b:	3d b6 00 00 00       	cmp    eax,0xb6
    1ea0:	0f 94 c0             	sete   al
    1ea3:	5d                   	pop    rbp
    1ea4:	c3                   	ret    

0000000000001ea5 <f6805295>:
    1ea5:	f3 0f 1e fa          	endbr64 
    1ea9:	55                   	push   rbp
    1eaa:	48 89 e5             	mov    rbp,rsp
    1ead:	89 f8                	mov    eax,edi
    1eaf:	88 45 fc             	mov    BYTE PTR [rbp-0x4],al
    1eb2:	0f be 45 fc          	movsx  eax,BYTE PTR [rbp-0x4]
    1eb6:	c1 e0 04             	shl    eax,0x4
    1eb9:	0f b6 d0             	movzx  edx,al
    1ebc:	0f b6 45 fc          	movzx  eax,BYTE PTR [rbp-0x4]
    1ec0:	c0 f8 04             	sar    al,0x4
    1ec3:	0f be c0             	movsx  eax,al
    1ec6:	01 d0                	add    eax,edx
    1ec8:	3d f5 00 00 00       	cmp    eax,0xf5
    1ecd:	0f 94 c0             	sete   al
    1ed0:	5d                   	pop    rbp
    1ed1:	c3                   	ret    

0000000000001ed2 <f7429348>:
    1ed2:	f3 0f 1e fa          	endbr64 
    1ed6:	55                   	push   rbp
    1ed7:	48 89 e5             	mov    rbp,rsp
    1eda:	89 f8                	mov    eax,edi
    1edc:	88 45 fc             	mov    BYTE PTR [rbp-0x4],al
    1edf:	0f be 45 fc          	movsx  eax,BYTE PTR [rbp-0x4]
    1ee3:	c1 e0 04             	shl    eax,0x4
    1ee6:	0f b6 d0             	movzx  edx,al
    1ee9:	0f b6 45 fc          	movzx  eax,BYTE PTR [rbp-0x4]
    1eed:	c0 f8 04             	sar    al,0x4
    1ef0:	0f be c0             	movsx  eax,al
    1ef3:	01 d0                	add    eax,edx
    1ef5:	3d 97 00 00 00       	cmp    eax,0x97
    1efa:	0f 94 c0             	sete   al
    1efd:	5d                   	pop    rbp
    1efe:	c3                   	ret    

0000000000001eff <f8265912>:
    1eff:	f3 0f 1e fa          	endbr64 
    1f03:	55                   	push   rbp
    1f04:	48 89 e5             	mov    rbp,rsp
    1f07:	89 f8                	mov    eax,edi
    1f09:	88 45 fc             	mov    BYTE PTR [rbp-0x4],al
    1f0c:	0f be 45 fc          	movsx  eax,BYTE PTR [rbp-0x4]
    1f10:	c1 e0 04             	shl    eax,0x4
    1f13:	0f b6 d0             	movzx  edx,al
    1f16:	0f b6 45 fc          	movzx  eax,BYTE PTR [rbp-0x4]
    1f1a:	c0 f8 04             	sar    al,0x4
    1f1d:	0f be c0             	movsx  eax,al
    1f20:	01 d0                	add    eax,edx
    1f22:	83 f8 03             	cmp    eax,0x3
    1f25:	0f 94 c0             	sete   al
    1f28:	5d                   	pop    rbp
    1f29:	c3                   	ret    

0000000000001f2a <f3580401>:
    1f2a:	f3 0f 1e fa          	endbr64 
    1f2e:	55                   	push   rbp
    1f2f:	48 89 e5             	mov    rbp,rsp
    1f32:	89 f8                	mov    eax,edi
    1f34:	88 45 fc             	mov    BYTE PTR [rbp-0x4],al
    1f37:	0f be 45 fc          	movsx  eax,BYTE PTR [rbp-0x4]
    1f3b:	c1 e0 04             	shl    eax,0x4
    1f3e:	0f b6 d0             	movzx  edx,al
    1f41:	0f b6 45 fc          	movzx  eax,BYTE PTR [rbp-0x4]
    1f45:	c0 f8 04             	sar    al,0x4
    1f48:	0f be c0             	movsx  eax,al
    1f4b:	01 d0                	add    eax,edx
    1f4d:	83 f8 57             	cmp    eax,0x57
    1f50:	0f 94 c0             	sete   al
    1f53:	5d                   	pop    rbp
    1f54:	c3                   	ret    

0000000000001f55 <f8346581>:
    1f55:	f3 0f 1e fa          	endbr64 
    1f59:	55                   	push   rbp
    1f5a:	48 89 e5             	mov    rbp,rsp
    1f5d:	89 f8                	mov    eax,edi
    1f5f:	88 45 fc             	mov    BYTE PTR [rbp-0x4],al
    1f62:	0f be 45 fc          	movsx  eax,BYTE PTR [rbp-0x4]
    1f66:	c1 e0 04             	shl    eax,0x4
    1f69:	0f b6 d0             	movzx  edx,al
    1f6c:	0f b6 45 fc          	movzx  eax,BYTE PTR [rbp-0x4]
    1f70:	c0 f8 04             	sar    al,0x4
    1f73:	0f be c0             	movsx  eax,al
    1f76:	01 d0                	add    eax,edx
    1f78:	3d f5 00 00 00       	cmp    eax,0xf5
    1f7d:	0f 94 c0             	sete   al
    1f80:	5d                   	pop    rbp
    1f81:	c3                   	ret    

0000000000001f82 <f5751977>:
    1f82:	f3 0f 1e fa          	endbr64 
    1f86:	55                   	push   rbp
    1f87:	48 89 e5             	mov    rbp,rsp
    1f8a:	89 f8                	mov    eax,edi
    1f8c:	88 45 fc             	mov    BYTE PTR [rbp-0x4],al
    1f8f:	0f be 45 fc          	movsx  eax,BYTE PTR [rbp-0x4]
    1f93:	c1 e0 04             	shl    eax,0x4
    1f96:	0f b6 d0             	movzx  edx,al
    1f99:	0f b6 45 fc          	movzx  eax,BYTE PTR [rbp-0x4]
    1f9d:	c0 f8 04             	sar    al,0x4
    1fa0:	0f be c0             	movsx  eax,al
    1fa3:	01 d0                	add    eax,edx
    1fa5:	83 f8 26             	cmp    eax,0x26
    1fa8:	0f 94 c0             	sete   al
    1fab:	5d                   	pop    rbp
    1fac:	c3                   	ret    

0000000000001fad <f3210599>:
    1fad:	f3 0f 1e fa          	endbr64 
    1fb1:	55                   	push   rbp
    1fb2:	48 89 e5             	mov    rbp,rsp
    1fb5:	89 f8                	mov    eax,edi
    1fb7:	88 45 fc             	mov    BYTE PTR [rbp-0x4],al
    1fba:	0f be 45 fc          	movsx  eax,BYTE PTR [rbp-0x4]
    1fbe:	c1 e0 04             	shl    eax,0x4
    1fc1:	0f b6 d0             	movzx  edx,al
    1fc4:	0f b6 45 fc          	movzx  eax,BYTE PTR [rbp-0x4]
    1fc8:	c0 f8 04             	sar    al,0x4
    1fcb:	0f be c0             	movsx  eax,al
    1fce:	01 d0                	add    eax,edx
    1fd0:	83 f8 33             	cmp    eax,0x33
    1fd3:	0f 94 c0             	sete   al
    1fd6:	5d                   	pop    rbp
    1fd7:	c3                   	ret    

0000000000001fd8 <f1415318>:
    1fd8:	f3 0f 1e fa          	endbr64 
    1fdc:	55                   	push   rbp
    1fdd:	48 89 e5             	mov    rbp,rsp
    1fe0:	89 f8                	mov    eax,edi
    1fe2:	88 45 fc             	mov    BYTE PTR [rbp-0x4],al
    1fe5:	0f be 45 fc          	movsx  eax,BYTE PTR [rbp-0x4]
    1fe9:	c1 e0 04             	shl    eax,0x4
    1fec:	0f b6 d0             	movzx  edx,al
    1fef:	0f b6 45 fc          	movzx  eax,BYTE PTR [rbp-0x4]
    1ff3:	c0 f8 04             	sar    al,0x4
    1ff6:	0f be c0             	movsx  eax,al
    1ff9:	01 d0                	add    eax,edx
    1ffb:	83 f8 47             	cmp    eax,0x47
    1ffe:	0f 94 c0             	sete   al
    2001:	5d                   	pop    rbp
    2002:	c3                   	ret    

0000000000002003 <f3734500>:
    2003:	f3 0f 1e fa          	endbr64 
    2007:	55                   	push   rbp
    2008:	48 89 e5             	mov    rbp,rsp
    200b:	89 f8                	mov    eax,edi
    200d:	88 45 fc             	mov    BYTE PTR [rbp-0x4],al
    2010:	0f be 45 fc          	movsx  eax,BYTE PTR [rbp-0x4]
    2014:	c1 e0 04             	shl    eax,0x4
    2017:	0f b6 d0             	movzx  edx,al
    201a:	0f b6 45 fc          	movzx  eax,BYTE PTR [rbp-0x4]
    201e:	c0 f8 04             	sar    al,0x4
    2021:	0f be c0             	movsx  eax,al
    2024:	01 d0                	add    eax,edx
    2026:	83 f8 47             	cmp    eax,0x47
    2029:	0f 94 c0             	sete   al
    202c:	5d                   	pop    rbp
    202d:	c3                   	ret    

000000000000202e <f8917722>:
    202e:	f3 0f 1e fa          	endbr64 
    2032:	55                   	push   rbp
    2033:	48 89 e5             	mov    rbp,rsp
    2036:	89 f8                	mov    eax,edi
    2038:	88 45 fc             	mov    BYTE PTR [rbp-0x4],al
    203b:	0f be 45 fc          	movsx  eax,BYTE PTR [rbp-0x4]
    203f:	c1 e0 04             	shl    eax,0x4
    2042:	0f b6 d0             	movzx  edx,al
    2045:	0f b6 45 fc          	movzx  eax,BYTE PTR [rbp-0x4]
    2049:	c0 f8 04             	sar    al,0x4
    204c:	0f be c0             	movsx  eax,al
    204f:	01 d0                	add    eax,edx
    2051:	83 f8 33             	cmp    eax,0x33
    2054:	0f 94 c0             	sete   al
    2057:	5d                   	pop    rbp
    2058:	c3                   	ret    

0000000000002059 <f7283249>:
    2059:	f3 0f 1e fa          	endbr64 
    205d:	55                   	push   rbp
    205e:	48 89 e5             	mov    rbp,rsp
    2061:	89 f8                	mov    eax,edi
    2063:	88 45 fc             	mov    BYTE PTR [rbp-0x4],al
    2066:	0f be 45 fc          	movsx  eax,BYTE PTR [rbp-0x4]
    206a:	c1 e0 04             	shl    eax,0x4
    206d:	0f b6 d0             	movzx  edx,al
    2070:	0f b6 45 fc          	movzx  eax,BYTE PTR [rbp-0x4]
    2074:	c0 f8 04             	sar    al,0x4
    2077:	0f be c0             	movsx  eax,al
    207a:	01 d0                	add    eax,edx
    207c:	83 f8 27             	cmp    eax,0x27
    207f:	0f 94 c0             	sete   al
    2082:	5d                   	pop    rbp
    2083:	c3                   	ret    

0000000000002084 <f8622882>:
    2084:	f3 0f 1e fa          	endbr64 
    2088:	55                   	push   rbp
    2089:	48 89 e5             	mov    rbp,rsp
    208c:	89 f8                	mov    eax,edi
    208e:	88 45 fc             	mov    BYTE PTR [rbp-0x4],al
    2091:	0f be 45 fc          	movsx  eax,BYTE PTR [rbp-0x4]
    2095:	c1 e0 04             	shl    eax,0x4
    2098:	0f b6 d0             	movzx  edx,al
    209b:	0f b6 45 fc          	movzx  eax,BYTE PTR [rbp-0x4]
    209f:	c0 f8 04             	sar    al,0x4
    20a2:	0f be c0             	movsx  eax,al
    20a5:	01 d0                	add    eax,edx
    20a7:	3d f5 00 00 00       	cmp    eax,0xf5
    20ac:	0f 94 c0             	sete   al
    20af:	5d                   	pop    rbp
    20b0:	c3                   	ret    

00000000000020b1 <f1221298>:
    20b1:	f3 0f 1e fa          	endbr64 
    20b5:	55                   	push   rbp
    20b6:	48 89 e5             	mov    rbp,rsp
    20b9:	89 f8                	mov    eax,edi
    20bb:	88 45 fc             	mov    BYTE PTR [rbp-0x4],al
    20be:	0f be 45 fc          	movsx  eax,BYTE PTR [rbp-0x4]
    20c2:	c1 e0 04             	shl    eax,0x4
    20c5:	0f b6 d0             	movzx  edx,al
    20c8:	0f b6 45 fc          	movzx  eax,BYTE PTR [rbp-0x4]
    20cc:	c0 f8 04             	sar    al,0x4
    20cf:	0f be c0             	movsx  eax,al
    20d2:	01 d0                	add    eax,edx
    20d4:	83 f8 57             	cmp    eax,0x57
    20d7:	0f 94 c0             	sete   al
    20da:	5d                   	pop    rbp
    20db:	c3                   	ret    

00000000000020dc <f2575656>:
    20dc:	f3 0f 1e fa          	endbr64 
    20e0:	55                   	push   rbp
    20e1:	48 89 e5             	mov    rbp,rsp
    20e4:	89 f8                	mov    eax,edi
    20e6:	88 45 fc             	mov    BYTE PTR [rbp-0x4],al
    20e9:	0f be 45 fc          	movsx  eax,BYTE PTR [rbp-0x4]
    20ed:	c1 e0 04             	shl    eax,0x4
    20f0:	0f b6 d0             	movzx  edx,al
    20f3:	0f b6 45 fc          	movzx  eax,BYTE PTR [rbp-0x4]
    20f7:	c0 f8 04             	sar    al,0x4
    20fa:	0f be c0             	movsx  eax,al
    20fd:	01 d0                	add    eax,edx
    20ff:	83 f8 37             	cmp    eax,0x37
    2102:	0f 94 c0             	sete   al
    2105:	5d                   	pop    rbp
    2106:	c3                   	ret    

0000000000002107 <f2048837>:
    2107:	f3 0f 1e fa          	endbr64 
    210b:	55                   	push   rbp
    210c:	48 89 e5             	mov    rbp,rsp
    210f:	89 f8                	mov    eax,edi
    2111:	88 45 fc             	mov    BYTE PTR [rbp-0x4],al
    2114:	0f be 45 fc          	movsx  eax,BYTE PTR [rbp-0x4]
    2118:	c1 e0 04             	shl    eax,0x4
    211b:	0f b6 d0             	movzx  edx,al
    211e:	0f b6 45 fc          	movzx  eax,BYTE PTR [rbp-0x4]
    2122:	c0 f8 04             	sar    al,0x4
    2125:	0f be c0             	movsx  eax,al
    2128:	01 d0                	add    eax,edx
    212a:	83 f8 33             	cmp    eax,0x33
    212d:	0f 94 c0             	sete   al
    2130:	5d                   	pop    rbp
    2131:	c3                   	ret    

0000000000002132 <f2256059>:
    2132:	f3 0f 1e fa          	endbr64 
    2136:	55                   	push   rbp
    2137:	48 89 e5             	mov    rbp,rsp
    213a:	89 f8                	mov    eax,edi
    213c:	88 45 fc             	mov    BYTE PTR [rbp-0x4],al
    213f:	0f be 45 fc          	movsx  eax,BYTE PTR [rbp-0x4]
    2143:	c1 e0 04             	shl    eax,0x4
    2146:	0f b6 d0             	movzx  edx,al
    2149:	0f b6 45 fc          	movzx  eax,BYTE PTR [rbp-0x4]
    214d:	c0 f8 04             	sar    al,0x4
    2150:	0f be c0             	movsx  eax,al
    2153:	01 d0                	add    eax,edx
    2155:	3d f5 00 00 00       	cmp    eax,0xf5
    215a:	0f 94 c0             	sete   al
    215d:	5d                   	pop    rbp
    215e:	c3                   	ret    

000000000000215f <f1257459>:
    215f:	f3 0f 1e fa          	endbr64 
    2163:	55                   	push   rbp
    2164:	48 89 e5             	mov    rbp,rsp
    2167:	89 f8                	mov    eax,edi
    2169:	88 45 fc             	mov    BYTE PTR [rbp-0x4],al
    216c:	0f be 45 fc          	movsx  eax,BYTE PTR [rbp-0x4]
    2170:	c1 e0 04             	shl    eax,0x4
    2173:	0f b6 d0             	movzx  edx,al
    2176:	0f b6 45 fc          	movzx  eax,BYTE PTR [rbp-0x4]
    217a:	c0 f8 04             	sar    al,0x4
    217d:	0f be c0             	movsx  eax,al
    2180:	01 d0                	add    eax,edx
    2182:	83 f8 37             	cmp    eax,0x37
    2185:	0f 94 c0             	sete   al
    2188:	5d                   	pop    rbp
    2189:	c3                   	ret    

000000000000218a <f5021108>:
    218a:	f3 0f 1e fa          	endbr64 
    218e:	55                   	push   rbp
    218f:	48 89 e5             	mov    rbp,rsp
    2192:	89 f8                	mov    eax,edi
    2194:	88 45 fc             	mov    BYTE PTR [rbp-0x4],al
    2197:	0f be 45 fc          	movsx  eax,BYTE PTR [rbp-0x4]
    219b:	c1 e0 04             	shl    eax,0x4
    219e:	0f b6 d0             	movzx  edx,al
    21a1:	0f b6 45 fc          	movzx  eax,BYTE PTR [rbp-0x4]
    21a5:	c0 f8 04             	sar    al,0x4
    21a8:	0f be c0             	movsx  eax,al
    21ab:	01 d0                	add    eax,edx
    21ad:	83 f8 03             	cmp    eax,0x3
    21b0:	0f 94 c0             	sete   al
    21b3:	5d                   	pop    rbp
    21b4:	c3                   	ret    

00000000000021b5 <f8183340>:
    21b5:	f3 0f 1e fa          	endbr64 
    21b9:	55                   	push   rbp
    21ba:	48 89 e5             	mov    rbp,rsp
    21bd:	89 f8                	mov    eax,edi
    21bf:	88 45 fc             	mov    BYTE PTR [rbp-0x4],al
    21c2:	0f be 45 fc          	movsx  eax,BYTE PTR [rbp-0x4]
    21c6:	c1 e0 04             	shl    eax,0x4
    21c9:	0f b6 d0             	movzx  edx,al
    21cc:	0f b6 45 fc          	movzx  eax,BYTE PTR [rbp-0x4]
    21d0:	c0 f8 04             	sar    al,0x4
    21d3:	0f be c0             	movsx  eax,al
    21d6:	01 d0                	add    eax,edx
    21d8:	3d d6 00 00 00       	cmp    eax,0xd6
    21dd:	0f 94 c0             	sete   al
    21e0:	5d                   	pop    rbp
    21e1:	c3                   	ret    

00000000000021e2 <f4188611>:
    21e2:	f3 0f 1e fa          	endbr64 
    21e6:	55                   	push   rbp
    21e7:	48 89 e5             	mov    rbp,rsp
    21ea:	89 f8                	mov    eax,edi
    21ec:	88 45 fc             	mov    BYTE PTR [rbp-0x4],al
    21ef:	0f be 45 fc          	movsx  eax,BYTE PTR [rbp-0x4]
    21f3:	c1 e0 04             	shl    eax,0x4
    21f6:	0f b6 d0             	movzx  edx,al
    21f9:	0f b6 45 fc          	movzx  eax,BYTE PTR [rbp-0x4]
    21fd:	c0 f8 04             	sar    al,0x4
    2200:	0f be c0             	movsx  eax,al
    2203:	01 d0                	add    eax,edx
    2205:	83 f8 33             	cmp    eax,0x33
    2208:	0f 94 c0             	sete   al
    220b:	5d                   	pop    rbp
    220c:	c3                   	ret    

000000000000220d <f7842102>:
    220d:	f3 0f 1e fa          	endbr64 
    2211:	55                   	push   rbp
    2212:	48 89 e5             	mov    rbp,rsp
    2215:	89 f8                	mov    eax,edi
    2217:	88 45 fc             	mov    BYTE PTR [rbp-0x4],al
    221a:	0f be 45 fc          	movsx  eax,BYTE PTR [rbp-0x4]
    221e:	c1 e0 04             	shl    eax,0x4
    2221:	0f b6 d0             	movzx  edx,al
    2224:	0f b6 45 fc          	movzx  eax,BYTE PTR [rbp-0x4]
    2228:	c0 f8 04             	sar    al,0x4
    222b:	0f be c0             	movsx  eax,al
    222e:	01 d0                	add    eax,edx
    2230:	3d f5 00 00 00       	cmp    eax,0xf5
    2235:	0f 94 c0             	sete   al
    2238:	5d                   	pop    rbp
    2239:	c3                   	ret    

000000000000223a <f5218775>:
    223a:	f3 0f 1e fa          	endbr64 
    223e:	55                   	push   rbp
    223f:	48 89 e5             	mov    rbp,rsp
    2242:	89 f8                	mov    eax,edi
    2244:	88 45 fc             	mov    BYTE PTR [rbp-0x4],al
    2247:	0f be 45 fc          	movsx  eax,BYTE PTR [rbp-0x4]
    224b:	c1 e0 04             	shl    eax,0x4
    224e:	0f b6 d0             	movzx  edx,al
    2251:	0f b6 45 fc          	movzx  eax,BYTE PTR [rbp-0x4]
    2255:	c0 f8 04             	sar    al,0x4
    2258:	0f be c0             	movsx  eax,al
    225b:	01 d0                	add    eax,edx
    225d:	83 f8 16             	cmp    eax,0x16
    2260:	0f 94 c0             	sete   al
    2263:	5d                   	pop    rbp
    2264:	c3                   	ret    

0000000000002265 <f8862806>:
    2265:	f3 0f 1e fa          	endbr64 
    2269:	55                   	push   rbp
    226a:	48 89 e5             	mov    rbp,rsp
    226d:	89 f8                	mov    eax,edi
    226f:	88 45 fc             	mov    BYTE PTR [rbp-0x4],al
    2272:	0f be 45 fc          	movsx  eax,BYTE PTR [rbp-0x4]
    2276:	c1 e0 04             	shl    eax,0x4
    2279:	0f b6 d0             	movzx  edx,al
    227c:	0f b6 45 fc          	movzx  eax,BYTE PTR [rbp-0x4]
    2280:	c0 f8 04             	sar    al,0x4
    2283:	0f be c0             	movsx  eax,al
    2286:	01 d0                	add    eax,edx
    2288:	83 f8 57             	cmp    eax,0x57
    228b:	0f 94 c0             	sete   al
    228e:	5d                   	pop    rbp
    228f:	c3                   	ret    

0000000000002290 <f7824321>:
    2290:	f3 0f 1e fa          	endbr64 
    2294:	55                   	push   rbp
    2295:	48 89 e5             	mov    rbp,rsp
    2298:	89 f8                	mov    eax,edi
    229a:	88 45 fc             	mov    BYTE PTR [rbp-0x4],al
    229d:	0f be 45 fc          	movsx  eax,BYTE PTR [rbp-0x4]
    22a1:	c1 e0 04             	shl    eax,0x4
    22a4:	0f b6 d0             	movzx  edx,al
    22a7:	0f b6 45 fc          	movzx  eax,BYTE PTR [rbp-0x4]
    22ab:	c0 f8 04             	sar    al,0x4
    22ae:	0f be c0             	movsx  eax,al
    22b1:	01 d0                	add    eax,edx
    22b3:	83 f8 47             	cmp    eax,0x47
    22b6:	0f 94 c0             	sete   al
    22b9:	5d                   	pop    rbp
    22ba:	c3                   	ret    

00000000000022bb <f3450917>:
    22bb:	f3 0f 1e fa          	endbr64 
    22bf:	55                   	push   rbp
    22c0:	48 89 e5             	mov    rbp,rsp
    22c3:	89 f8                	mov    eax,edi
    22c5:	88 45 fc             	mov    BYTE PTR [rbp-0x4],al
    22c8:	0f be 45 fc          	movsx  eax,BYTE PTR [rbp-0x4]
    22cc:	c1 e0 04             	shl    eax,0x4
    22cf:	0f b6 d0             	movzx  edx,al
    22d2:	0f b6 45 fc          	movzx  eax,BYTE PTR [rbp-0x4]
    22d6:	c0 f8 04             	sar    al,0x4
    22d9:	0f be c0             	movsx  eax,al
    22dc:	01 d0                	add    eax,edx
    22de:	83 f8 03             	cmp    eax,0x3
    22e1:	0f 94 c0             	sete   al
    22e4:	5d                   	pop    rbp
    22e5:	c3                   	ret    

00000000000022e6 <f1224443>:
    22e6:	f3 0f 1e fa          	endbr64 
    22ea:	55                   	push   rbp
    22eb:	48 89 e5             	mov    rbp,rsp
    22ee:	89 f8                	mov    eax,edi
    22f0:	88 45 fc             	mov    BYTE PTR [rbp-0x4],al
    22f3:	0f be 45 fc          	movsx  eax,BYTE PTR [rbp-0x4]
    22f7:	c1 e0 04             	shl    eax,0x4
    22fa:	0f b6 d0             	movzx  edx,al
    22fd:	0f b6 45 fc          	movzx  eax,BYTE PTR [rbp-0x4]
    2301:	c0 f8 04             	sar    al,0x4
    2304:	0f be c0             	movsx  eax,al
    2307:	01 d0                	add    eax,edx
    2309:	3d d6 00 00 00       	cmp    eax,0xd6
    230e:	0f 94 c0             	sete   al
    2311:	5d                   	pop    rbp
    2312:	c3                   	ret    

0000000000002313 <f1210252>:
    2313:	f3 0f 1e fa          	endbr64 
    2317:	55                   	push   rbp
    2318:	48 89 e5             	mov    rbp,rsp
    231b:	89 f8                	mov    eax,edi
    231d:	88 45 fc             	mov    BYTE PTR [rbp-0x4],al
    2320:	0f be 45 fc          	movsx  eax,BYTE PTR [rbp-0x4]
    2324:	c1 e0 04             	shl    eax,0x4
    2327:	0f b6 d0             	movzx  edx,al
    232a:	0f b6 45 fc          	movzx  eax,BYTE PTR [rbp-0x4]
    232e:	c0 f8 04             	sar    al,0x4
    2331:	0f be c0             	movsx  eax,al
    2334:	01 d0                	add    eax,edx
    2336:	83 f8 43             	cmp    eax,0x43
    2339:	0f 94 c0             	sete   al
    233c:	5d                   	pop    rbp
    233d:	c3                   	ret    

000000000000233e <f1011265>:
    233e:	f3 0f 1e fa          	endbr64 
    2342:	55                   	push   rbp
    2343:	48 89 e5             	mov    rbp,rsp
    2346:	89 f8                	mov    eax,edi
    2348:	88 45 fc             	mov    BYTE PTR [rbp-0x4],al
    234b:	0f be 45 fc          	movsx  eax,BYTE PTR [rbp-0x4]
    234f:	c1 e0 04             	shl    eax,0x4
    2352:	0f b6 d0             	movzx  edx,al
    2355:	0f b6 45 fc          	movzx  eax,BYTE PTR [rbp-0x4]
    2359:	c0 f8 04             	sar    al,0x4
    235c:	0f be c0             	movsx  eax,al
    235f:	01 d0                	add    eax,edx
    2361:	83 f8 47             	cmp    eax,0x47
    2364:	0f 94 c0             	sete   al
    2367:	5d                   	pop    rbp
    2368:	c3                   	ret    

0000000000002369 <f8011510>:
    2369:	f3 0f 1e fa          	endbr64 
    236d:	55                   	push   rbp
    236e:	48 89 e5             	mov    rbp,rsp
    2371:	89 f8                	mov    eax,edi
    2373:	88 45 fc             	mov    BYTE PTR [rbp-0x4],al
    2376:	0f be 45 fc          	movsx  eax,BYTE PTR [rbp-0x4]
    237a:	c1 e0 04             	shl    eax,0x4
    237d:	0f b6 d0             	movzx  edx,al
    2380:	0f b6 45 fc          	movzx  eax,BYTE PTR [rbp-0x4]
    2384:	c0 f8 04             	sar    al,0x4
    2387:	0f be c0             	movsx  eax,al
    238a:	01 d0                	add    eax,edx
    238c:	83 f8 33             	cmp    eax,0x33
    238f:	0f 94 c0             	sete   al
    2392:	5d                   	pop    rbp
    2393:	c3                   	ret    

0000000000002394 <f1083193>:
    2394:	f3 0f 1e fa          	endbr64 
    2398:	55                   	push   rbp
    2399:	48 89 e5             	mov    rbp,rsp
    239c:	89 f8                	mov    eax,edi
    239e:	88 45 fc             	mov    BYTE PTR [rbp-0x4],al
    23a1:	0f be 45 fc          	movsx  eax,BYTE PTR [rbp-0x4]
    23a5:	c1 e0 04             	shl    eax,0x4
    23a8:	0f b6 d0             	movzx  edx,al
    23ab:	0f b6 45 fc          	movzx  eax,BYTE PTR [rbp-0x4]
    23af:	c0 f8 04             	sar    al,0x4
    23b2:	0f be c0             	movsx  eax,al
    23b5:	01 d0                	add    eax,edx
    23b7:	83 f8 46             	cmp    eax,0x46
    23ba:	0f 94 c0             	sete   al
    23bd:	5d                   	pop    rbp
    23be:	c3                   	ret    

00000000000023bf <f2547905>:
    23bf:	f3 0f 1e fa          	endbr64 
    23c3:	55                   	push   rbp
    23c4:	48 89 e5             	mov    rbp,rsp
    23c7:	89 f8                	mov    eax,edi
    23c9:	88 45 fc             	mov    BYTE PTR [rbp-0x4],al
    23cc:	0f be 45 fc          	movsx  eax,BYTE PTR [rbp-0x4]
    23d0:	c1 e0 04             	shl    eax,0x4
    23d3:	0f b6 d0             	movzx  edx,al
    23d6:	0f b6 45 fc          	movzx  eax,BYTE PTR [rbp-0x4]
    23da:	c0 f8 04             	sar    al,0x4
    23dd:	0f be c0             	movsx  eax,al
    23e0:	01 d0                	add    eax,edx
    23e2:	3d f5 00 00 00       	cmp    eax,0xf5
    23e7:	0f 94 c0             	sete   al
    23ea:	5d                   	pop    rbp
    23eb:	c3                   	ret    

00000000000023ec <f5585047>:
    23ec:	f3 0f 1e fa          	endbr64 
    23f0:	55                   	push   rbp
    23f1:	48 89 e5             	mov    rbp,rsp
    23f4:	89 f8                	mov    eax,edi
    23f6:	88 45 fc             	mov    BYTE PTR [rbp-0x4],al
    23f9:	0f be 45 fc          	movsx  eax,BYTE PTR [rbp-0x4]
    23fd:	c1 e0 04             	shl    eax,0x4
    2400:	0f b6 d0             	movzx  edx,al
    2403:	0f b6 45 fc          	movzx  eax,BYTE PTR [rbp-0x4]
    2407:	c0 f8 04             	sar    al,0x4
    240a:	0f be c0             	movsx  eax,al
    240d:	01 d0                	add    eax,edx
    240f:	83 f8 47             	cmp    eax,0x47
    2412:	0f 94 c0             	sete   al
    2415:	5d                   	pop    rbp
    2416:	c3                   	ret    

0000000000002417 <f9747250>:
    2417:	f3 0f 1e fa          	endbr64 
    241b:	55                   	push   rbp
    241c:	48 89 e5             	mov    rbp,rsp
    241f:	89 f8                	mov    eax,edi
    2421:	88 45 fc             	mov    BYTE PTR [rbp-0x4],al
    2424:	0f be 45 fc          	movsx  eax,BYTE PTR [rbp-0x4]
    2428:	c1 e0 04             	shl    eax,0x4
    242b:	0f b6 d0             	movzx  edx,al
    242e:	0f b6 45 fc          	movzx  eax,BYTE PTR [rbp-0x4]
    2432:	c0 f8 04             	sar    al,0x4
    2435:	0f be c0             	movsx  eax,al
    2438:	01 d0                	add    eax,edx
    243a:	83 f8 03             	cmp    eax,0x3
    243d:	0f 94 c0             	sete   al
    2440:	5d                   	pop    rbp
    2441:	c3                   	ret    

0000000000002442 <f2454679>:
    2442:	f3 0f 1e fa          	endbr64 
    2446:	55                   	push   rbp
    2447:	48 89 e5             	mov    rbp,rsp
    244a:	89 f8                	mov    eax,edi
    244c:	88 45 fc             	mov    BYTE PTR [rbp-0x4],al
    244f:	0f be 45 fc          	movsx  eax,BYTE PTR [rbp-0x4]
    2453:	c1 e0 04             	shl    eax,0x4
    2456:	0f b6 d0             	movzx  edx,al
    2459:	0f b6 45 fc          	movzx  eax,BYTE PTR [rbp-0x4]
    245d:	c0 f8 04             	sar    al,0x4
    2460:	0f be c0             	movsx  eax,al
    2463:	01 d0                	add    eax,edx
    2465:	83 f8 03             	cmp    eax,0x3
    2468:	0f 94 c0             	sete   al
    246b:	5d                   	pop    rbp
    246c:	c3                   	ret    

000000000000246d <f5724032>:
    246d:	f3 0f 1e fa          	endbr64 
    2471:	55                   	push   rbp
    2472:	48 89 e5             	mov    rbp,rsp
    2475:	89 f8                	mov    eax,edi
    2477:	88 45 fc             	mov    BYTE PTR [rbp-0x4],al
    247a:	0f be 45 fc          	movsx  eax,BYTE PTR [rbp-0x4]
    247e:	c1 e0 04             	shl    eax,0x4
    2481:	0f b6 d0             	movzx  edx,al
    2484:	0f b6 45 fc          	movzx  eax,BYTE PTR [rbp-0x4]
    2488:	c0 f8 04             	sar    al,0x4
    248b:	0f be c0             	movsx  eax,al
    248e:	01 d0                	add    eax,edx
    2490:	3d c6 00 00 00       	cmp    eax,0xc6
    2495:	0f 94 c0             	sete   al
    2498:	5d                   	pop    rbp
    2499:	c3                   	ret    

000000000000249a <f1871302>:
    249a:	f3 0f 1e fa          	endbr64 
    249e:	55                   	push   rbp
    249f:	48 89 e5             	mov    rbp,rsp
    24a2:	89 f8                	mov    eax,edi
    24a4:	88 45 fc             	mov    BYTE PTR [rbp-0x4],al
    24a7:	0f be 45 fc          	movsx  eax,BYTE PTR [rbp-0x4]
    24ab:	c1 e0 04             	shl    eax,0x4
    24ae:	0f b6 d0             	movzx  edx,al
    24b1:	0f b6 45 fc          	movzx  eax,BYTE PTR [rbp-0x4]
    24b5:	c0 f8 04             	sar    al,0x4
    24b8:	0f be c0             	movsx  eax,al
    24bb:	01 d0                	add    eax,edx
    24bd:	83 f8 37             	cmp    eax,0x37
    24c0:	0f 94 c0             	sete   al
    24c3:	5d                   	pop    rbp
    24c4:	c3                   	ret    

00000000000024c5 <f4168763>:
    24c5:	f3 0f 1e fa          	endbr64 
    24c9:	55                   	push   rbp
    24ca:	48 89 e5             	mov    rbp,rsp
    24cd:	89 f8                	mov    eax,edi
    24cf:	88 45 fc             	mov    BYTE PTR [rbp-0x4],al
    24d2:	0f be 45 fc          	movsx  eax,BYTE PTR [rbp-0x4]
    24d6:	c1 e0 04             	shl    eax,0x4
    24d9:	0f b6 d0             	movzx  edx,al
    24dc:	0f b6 45 fc          	movzx  eax,BYTE PTR [rbp-0x4]
    24e0:	c0 f8 04             	sar    al,0x4
    24e3:	0f be c0             	movsx  eax,al
    24e6:	01 d0                	add    eax,edx
    24e8:	3d f5 00 00 00       	cmp    eax,0xf5
    24ed:	0f 94 c0             	sete   al
    24f0:	5d                   	pop    rbp
    24f1:	c3                   	ret    

00000000000024f2 <f3207138>:
    24f2:	f3 0f 1e fa          	endbr64 
    24f6:	55                   	push   rbp
    24f7:	48 89 e5             	mov    rbp,rsp
    24fa:	89 f8                	mov    eax,edi
    24fc:	88 45 fc             	mov    BYTE PTR [rbp-0x4],al
    24ff:	0f be 45 fc          	movsx  eax,BYTE PTR [rbp-0x4]
    2503:	c1 e0 04             	shl    eax,0x4
    2506:	0f b6 d0             	movzx  edx,al
    2509:	0f b6 45 fc          	movzx  eax,BYTE PTR [rbp-0x4]
    250d:	c0 f8 04             	sar    al,0x4
    2510:	0f be c0             	movsx  eax,al
    2513:	01 d0                	add    eax,edx
    2515:	3d c6 00 00 00       	cmp    eax,0xc6
    251a:	0f 94 c0             	sete   al
    251d:	5d                   	pop    rbp
    251e:	c3                   	ret    

000000000000251f <f4692198>:
    251f:	f3 0f 1e fa          	endbr64 
    2523:	55                   	push   rbp
    2524:	48 89 e5             	mov    rbp,rsp
    2527:	89 f8                	mov    eax,edi
    2529:	88 45 fc             	mov    BYTE PTR [rbp-0x4],al
    252c:	0f be 45 fc          	movsx  eax,BYTE PTR [rbp-0x4]
    2530:	c1 e0 04             	shl    eax,0x4
    2533:	0f b6 d0             	movzx  edx,al
    2536:	0f b6 45 fc          	movzx  eax,BYTE PTR [rbp-0x4]
    253a:	c0 f8 04             	sar    al,0x4
    253d:	0f be c0             	movsx  eax,al
    2540:	01 d0                	add    eax,edx
    2542:	83 f8 13             	cmp    eax,0x13
    2545:	0f 94 c0             	sete   al
    2548:	5d                   	pop    rbp
    2549:	c3                   	ret    

000000000000254a <f518159>:
    254a:	f3 0f 1e fa          	endbr64 
    254e:	55                   	push   rbp
    254f:	48 89 e5             	mov    rbp,rsp
    2552:	89 f8                	mov    eax,edi
    2554:	88 45 fc             	mov    BYTE PTR [rbp-0x4],al
    2557:	0f be 45 fc          	movsx  eax,BYTE PTR [rbp-0x4]
    255b:	c1 e0 04             	shl    eax,0x4
    255e:	0f b6 d0             	movzx  edx,al
    2561:	0f b6 45 fc          	movzx  eax,BYTE PTR [rbp-0x4]
    2565:	c0 f8 04             	sar    al,0x4
    2568:	0f be c0             	movsx  eax,al
    256b:	01 d0                	add    eax,edx
    256d:	3d b6 00 00 00       	cmp    eax,0xb6
    2572:	0f 94 c0             	sete   al
    2575:	5d                   	pop    rbp
    2576:	c3                   	ret    

0000000000002577 <f1762925>:
    2577:	f3 0f 1e fa          	endbr64 
    257b:	55                   	push   rbp
    257c:	48 89 e5             	mov    rbp,rsp
    257f:	89 f8                	mov    eax,edi
    2581:	88 45 fc             	mov    BYTE PTR [rbp-0x4],al
    2584:	0f be 45 fc          	movsx  eax,BYTE PTR [rbp-0x4]
    2588:	c1 e0 04             	shl    eax,0x4
    258b:	0f b6 d0             	movzx  edx,al
    258e:	0f b6 45 fc          	movzx  eax,BYTE PTR [rbp-0x4]
    2592:	c0 f8 04             	sar    al,0x4
    2595:	0f be c0             	movsx  eax,al
    2598:	01 d0                	add    eax,edx
    259a:	83 f8 33             	cmp    eax,0x33
    259d:	0f 94 c0             	sete   al
    25a0:	5d                   	pop    rbp
    25a1:	c3                   	ret    

00000000000025a2 <f6594036>:
    25a2:	f3 0f 1e fa          	endbr64 
    25a6:	55                   	push   rbp
    25a7:	48 89 e5             	mov    rbp,rsp
    25aa:	89 f8                	mov    eax,edi
    25ac:	88 45 fc             	mov    BYTE PTR [rbp-0x4],al
    25af:	0f be 45 fc          	movsx  eax,BYTE PTR [rbp-0x4]
    25b3:	c1 e0 04             	shl    eax,0x4
    25b6:	0f b6 d0             	movzx  edx,al
    25b9:	0f b6 45 fc          	movzx  eax,BYTE PTR [rbp-0x4]
    25bd:	c0 f8 04             	sar    al,0x4
    25c0:	0f be c0             	movsx  eax,al
    25c3:	01 d0                	add    eax,edx
    25c5:	3d f5 00 00 00       	cmp    eax,0xf5
    25ca:	0f 94 c0             	sete   al
    25cd:	5d                   	pop    rbp
    25ce:	c3                   	ret    

00000000000025cf <f4698560>:
    25cf:	f3 0f 1e fa          	endbr64 
    25d3:	55                   	push   rbp
    25d4:	48 89 e5             	mov    rbp,rsp
    25d7:	89 f8                	mov    eax,edi
    25d9:	88 45 fc             	mov    BYTE PTR [rbp-0x4],al
    25dc:	0f be 45 fc          	movsx  eax,BYTE PTR [rbp-0x4]
    25e0:	c1 e0 04             	shl    eax,0x4
    25e3:	0f b6 d0             	movzx  edx,al
    25e6:	0f b6 45 fc          	movzx  eax,BYTE PTR [rbp-0x4]
    25ea:	c0 f8 04             	sar    al,0x4
    25ed:	0f be c0             	movsx  eax,al
    25f0:	01 d0                	add    eax,edx
    25f2:	83 f8 43             	cmp    eax,0x43
    25f5:	0f 94 c0             	sete   al
    25f8:	5d                   	pop    rbp
    25f9:	c3                   	ret    

00000000000025fa <f51135>:
    25fa:	f3 0f 1e fa          	endbr64 
    25fe:	55                   	push   rbp
    25ff:	48 89 e5             	mov    rbp,rsp
    2602:	89 f8                	mov    eax,edi
    2604:	88 45 fc             	mov    BYTE PTR [rbp-0x4],al
    2607:	0f be 45 fc          	movsx  eax,BYTE PTR [rbp-0x4]
    260b:	c1 e0 04             	shl    eax,0x4
    260e:	0f b6 d0             	movzx  edx,al
    2611:	0f b6 45 fc          	movzx  eax,BYTE PTR [rbp-0x4]
    2615:	c0 f8 04             	sar    al,0x4
    2618:	0f be c0             	movsx  eax,al
    261b:	01 d0                	add    eax,edx
    261d:	3d e6 00 00 00       	cmp    eax,0xe6
    2622:	0f 94 c0             	sete   al
    2625:	5d                   	pop    rbp
    2626:	c3                   	ret    

0000000000002627 <f2844159>:
    2627:	f3 0f 1e fa          	endbr64 
    262b:	55                   	push   rbp
    262c:	48 89 e5             	mov    rbp,rsp
    262f:	89 f8                	mov    eax,edi
    2631:	88 45 fc             	mov    BYTE PTR [rbp-0x4],al
    2634:	0f be 45 fc          	movsx  eax,BYTE PTR [rbp-0x4]
    2638:	c1 e0 04             	shl    eax,0x4
    263b:	0f b6 d0             	movzx  edx,al
    263e:	0f b6 45 fc          	movzx  eax,BYTE PTR [rbp-0x4]
    2642:	c0 f8 04             	sar    al,0x4
    2645:	0f be c0             	movsx  eax,al
    2648:	01 d0                	add    eax,edx
    264a:	3d 93 00 00 00       	cmp    eax,0x93
    264f:	0f 94 c0             	sete   al
    2652:	5d                   	pop    rbp
    2653:	c3                   	ret    

0000000000002654 <f5858457>:
    2654:	f3 0f 1e fa          	endbr64 
    2658:	55                   	push   rbp
    2659:	48 89 e5             	mov    rbp,rsp
    265c:	89 f8                	mov    eax,edi
    265e:	88 45 fc             	mov    BYTE PTR [rbp-0x4],al
    2661:	0f be 45 fc          	movsx  eax,BYTE PTR [rbp-0x4]
    2665:	c1 e0 04             	shl    eax,0x4
    2668:	0f b6 d0             	movzx  edx,al
    266b:	0f b6 45 fc          	movzx  eax,BYTE PTR [rbp-0x4]
    266f:	c0 f8 04             	sar    al,0x4
    2672:	0f be c0             	movsx  eax,al
    2675:	01 d0                	add    eax,edx
    2677:	83 f8 27             	cmp    eax,0x27
    267a:	0f 94 c0             	sete   al
    267d:	5d                   	pop    rbp
    267e:	c3                   	ret    

000000000000267f <f2731283>:
    267f:	f3 0f 1e fa          	endbr64 
    2683:	55                   	push   rbp
    2684:	48 89 e5             	mov    rbp,rsp
    2687:	89 f8                	mov    eax,edi
    2689:	88 45 fc             	mov    BYTE PTR [rbp-0x4],al
    268c:	0f be 45 fc          	movsx  eax,BYTE PTR [rbp-0x4]
    2690:	c1 e0 04             	shl    eax,0x4
    2693:	0f b6 d0             	movzx  edx,al
    2696:	0f b6 45 fc          	movzx  eax,BYTE PTR [rbp-0x4]
    269a:	c0 f8 04             	sar    al,0x4
    269d:	0f be c0             	movsx  eax,al
    26a0:	01 d0                	add    eax,edx
    26a2:	3d f5 00 00 00       	cmp    eax,0xf5
    26a7:	0f 94 c0             	sete   al
    26aa:	5d                   	pop    rbp
    26ab:	c3                   	ret    

00000000000026ac <f7538802>:
    26ac:	f3 0f 1e fa          	endbr64 
    26b0:	55                   	push   rbp
    26b1:	48 89 e5             	mov    rbp,rsp
    26b4:	89 f8                	mov    eax,edi
    26b6:	88 45 fc             	mov    BYTE PTR [rbp-0x4],al
    26b9:	0f be 45 fc          	movsx  eax,BYTE PTR [rbp-0x4]
    26bd:	c1 e0 04             	shl    eax,0x4
    26c0:	0f b6 d0             	movzx  edx,al
    26c3:	0f b6 45 fc          	movzx  eax,BYTE PTR [rbp-0x4]
    26c7:	c0 f8 04             	sar    al,0x4
    26ca:	0f be c0             	movsx  eax,al
    26cd:	01 d0                	add    eax,edx
    26cf:	83 f8 03             	cmp    eax,0x3
    26d2:	0f 94 c0             	sete   al
    26d5:	5d                   	pop    rbp
    26d6:	c3                   	ret    

00000000000026d7 <f3273483>:
    26d7:	f3 0f 1e fa          	endbr64 
    26db:	55                   	push   rbp
    26dc:	48 89 e5             	mov    rbp,rsp
    26df:	89 f8                	mov    eax,edi
    26e1:	88 45 fc             	mov    BYTE PTR [rbp-0x4],al
    26e4:	0f be 45 fc          	movsx  eax,BYTE PTR [rbp-0x4]
    26e8:	c1 e0 04             	shl    eax,0x4
    26eb:	0f b6 d0             	movzx  edx,al
    26ee:	0f b6 45 fc          	movzx  eax,BYTE PTR [rbp-0x4]
    26f2:	c0 f8 04             	sar    al,0x4
    26f5:	0f be c0             	movsx  eax,al
    26f8:	01 d0                	add    eax,edx
    26fa:	83 f8 27             	cmp    eax,0x27
    26fd:	0f 94 c0             	sete   al
    2700:	5d                   	pop    rbp
    2701:	c3                   	ret    

0000000000002702 <f6794679>:
    2702:	f3 0f 1e fa          	endbr64 
    2706:	55                   	push   rbp
    2707:	48 89 e5             	mov    rbp,rsp
    270a:	89 f8                	mov    eax,edi
    270c:	88 45 fc             	mov    BYTE PTR [rbp-0x4],al
    270f:	0f be 45 fc          	movsx  eax,BYTE PTR [rbp-0x4]
    2713:	c1 e0 04             	shl    eax,0x4
    2716:	0f b6 d0             	movzx  edx,al
    2719:	0f b6 45 fc          	movzx  eax,BYTE PTR [rbp-0x4]
    271d:	c0 f8 04             	sar    al,0x4
    2720:	0f be c0             	movsx  eax,al
    2723:	01 d0                	add    eax,edx
    2725:	3d f5 00 00 00       	cmp    eax,0xf5
    272a:	0f 94 c0             	sete   al
    272d:	5d                   	pop    rbp
    272e:	c3                   	ret    

000000000000272f <f9560420>:
    272f:	f3 0f 1e fa          	endbr64 
    2733:	55                   	push   rbp
    2734:	48 89 e5             	mov    rbp,rsp
    2737:	89 f8                	mov    eax,edi
    2739:	88 45 fc             	mov    BYTE PTR [rbp-0x4],al
    273c:	0f be 45 fc          	movsx  eax,BYTE PTR [rbp-0x4]
    2740:	c1 e0 04             	shl    eax,0x4
    2743:	0f b6 d0             	movzx  edx,al
    2746:	0f b6 45 fc          	movzx  eax,BYTE PTR [rbp-0x4]
    274a:	c0 f8 04             	sar    al,0x4
    274d:	0f be c0             	movsx  eax,al
    2750:	01 d0                	add    eax,edx
    2752:	3d a5 00 00 00       	cmp    eax,0xa5
    2757:	0f 94 c0             	sete   al
    275a:	5d                   	pop    rbp
    275b:	c3                   	ret    

000000000000275c <f3026215>:
    275c:	f3 0f 1e fa          	endbr64 
    2760:	55                   	push   rbp
    2761:	48 89 e5             	mov    rbp,rsp
    2764:	89 f8                	mov    eax,edi
    2766:	88 45 fc             	mov    BYTE PTR [rbp-0x4],al
    2769:	0f be 45 fc          	movsx  eax,BYTE PTR [rbp-0x4]
    276d:	c1 e0 04             	shl    eax,0x4
    2770:	0f b6 d0             	movzx  edx,al
    2773:	0f b6 45 fc          	movzx  eax,BYTE PTR [rbp-0x4]
    2777:	c0 f8 04             	sar    al,0x4
    277a:	0f be c0             	movsx  eax,al
    277d:	01 d0                	add    eax,edx
    277f:	83 f8 33             	cmp    eax,0x33
    2782:	0f 94 c0             	sete   al
    2785:	5d                   	pop    rbp
    2786:	c3                   	ret    

0000000000002787 <f4703035>:
    2787:	f3 0f 1e fa          	endbr64 
    278b:	55                   	push   rbp
    278c:	48 89 e5             	mov    rbp,rsp
    278f:	89 f8                	mov    eax,edi
    2791:	88 45 fc             	mov    BYTE PTR [rbp-0x4],al
    2794:	0f be 45 fc          	movsx  eax,BYTE PTR [rbp-0x4]
    2798:	c1 e0 04             	shl    eax,0x4
    279b:	0f b6 d0             	movzx  edx,al
    279e:	0f b6 45 fc          	movzx  eax,BYTE PTR [rbp-0x4]
    27a2:	c0 f8 04             	sar    al,0x4
    27a5:	0f be c0             	movsx  eax,al
    27a8:	01 d0                	add    eax,edx
    27aa:	3d f5 00 00 00       	cmp    eax,0xf5
    27af:	0f 94 c0             	sete   al
    27b2:	5d                   	pop    rbp
    27b3:	c3                   	ret    

00000000000027b4 <f7480532>:
    27b4:	f3 0f 1e fa          	endbr64 
    27b8:	55                   	push   rbp
    27b9:	48 89 e5             	mov    rbp,rsp
    27bc:	89 f8                	mov    eax,edi
    27be:	88 45 fc             	mov    BYTE PTR [rbp-0x4],al
    27c1:	0f be 45 fc          	movsx  eax,BYTE PTR [rbp-0x4]
    27c5:	c1 e0 04             	shl    eax,0x4
    27c8:	0f b6 d0             	movzx  edx,al
    27cb:	0f b6 45 fc          	movzx  eax,BYTE PTR [rbp-0x4]
    27cf:	c0 f8 04             	sar    al,0x4
    27d2:	0f be c0             	movsx  eax,al
    27d5:	01 d0                	add    eax,edx
    27d7:	83 f8 47             	cmp    eax,0x47
    27da:	0f 94 c0             	sete   al
    27dd:	5d                   	pop    rbp
    27de:	c3                   	ret    

00000000000027df <f8746401>:
    27df:	f3 0f 1e fa          	endbr64 
    27e3:	55                   	push   rbp
    27e4:	48 89 e5             	mov    rbp,rsp
    27e7:	89 f8                	mov    eax,edi
    27e9:	88 45 fc             	mov    BYTE PTR [rbp-0x4],al
    27ec:	0f be 45 fc          	movsx  eax,BYTE PTR [rbp-0x4]
    27f0:	c1 e0 04             	shl    eax,0x4
    27f3:	0f b6 d0             	movzx  edx,al
    27f6:	0f b6 45 fc          	movzx  eax,BYTE PTR [rbp-0x4]
    27fa:	c0 f8 04             	sar    al,0x4
    27fd:	0f be c0             	movsx  eax,al
    2800:	01 d0                	add    eax,edx
    2802:	83 f8 03             	cmp    eax,0x3
    2805:	0f 94 c0             	sete   al
    2808:	5d                   	pop    rbp
    2809:	c3                   	ret    

000000000000280a <f1223611>:
    280a:	f3 0f 1e fa          	endbr64 
    280e:	55                   	push   rbp
    280f:	48 89 e5             	mov    rbp,rsp
    2812:	89 f8                	mov    eax,edi
    2814:	88 45 fc             	mov    BYTE PTR [rbp-0x4],al
    2817:	0f be 45 fc          	movsx  eax,BYTE PTR [rbp-0x4]
    281b:	c1 e0 04             	shl    eax,0x4
    281e:	0f b6 d0             	movzx  edx,al
    2821:	0f b6 45 fc          	movzx  eax,BYTE PTR [rbp-0x4]
    2825:	c0 f8 04             	sar    al,0x4
    2828:	0f be c0             	movsx  eax,al
    282b:	01 d0                	add    eax,edx
    282d:	3d f5 00 00 00       	cmp    eax,0xf5
    2832:	0f 94 c0             	sete   al
    2835:	5d                   	pop    rbp
    2836:	c3                   	ret    

0000000000002837 <f9386630>:
    2837:	f3 0f 1e fa          	endbr64 
    283b:	55                   	push   rbp
    283c:	48 89 e5             	mov    rbp,rsp
    283f:	89 f8                	mov    eax,edi
    2841:	88 45 fc             	mov    BYTE PTR [rbp-0x4],al
    2844:	0f be 45 fc          	movsx  eax,BYTE PTR [rbp-0x4]
    2848:	c1 e0 04             	shl    eax,0x4
    284b:	0f b6 d0             	movzx  edx,al
    284e:	0f b6 45 fc          	movzx  eax,BYTE PTR [rbp-0x4]
    2852:	c0 f8 04             	sar    al,0x4
    2855:	0f be c0             	movsx  eax,al
    2858:	01 d0                	add    eax,edx
    285a:	3d d6 00 00 00       	cmp    eax,0xd6
    285f:	0f 94 c0             	sete   al
    2862:	5d                   	pop    rbp
    2863:	c3                   	ret    

0000000000002864 <f7022724>:
    2864:	f3 0f 1e fa          	endbr64 
    2868:	55                   	push   rbp
    2869:	48 89 e5             	mov    rbp,rsp
    286c:	89 f8                	mov    eax,edi
    286e:	88 45 fc             	mov    BYTE PTR [rbp-0x4],al
    2871:	0f be 45 fc          	movsx  eax,BYTE PTR [rbp-0x4]
    2875:	c1 e0 04             	shl    eax,0x4
    2878:	0f b6 d0             	movzx  edx,al
    287b:	0f b6 45 fc          	movzx  eax,BYTE PTR [rbp-0x4]
    287f:	c0 f8 04             	sar    al,0x4
    2882:	0f be c0             	movsx  eax,al
    2885:	01 d0                	add    eax,edx
    2887:	83 f8 43             	cmp    eax,0x43
    288a:	0f 94 c0             	sete   al
    288d:	5d                   	pop    rbp
    288e:	c3                   	ret    

000000000000288f <f6626111>:
    288f:	f3 0f 1e fa          	endbr64 
    2893:	55                   	push   rbp
    2894:	48 89 e5             	mov    rbp,rsp
    2897:	89 f8                	mov    eax,edi
    2899:	88 45 fc             	mov    BYTE PTR [rbp-0x4],al
    289c:	0f be 45 fc          	movsx  eax,BYTE PTR [rbp-0x4]
    28a0:	c1 e0 04             	shl    eax,0x4
    28a3:	0f b6 d0             	movzx  edx,al
    28a6:	0f b6 45 fc          	movzx  eax,BYTE PTR [rbp-0x4]
    28aa:	c0 f8 04             	sar    al,0x4
    28ad:	0f be c0             	movsx  eax,al
    28b0:	01 d0                	add    eax,edx
    28b2:	3d b6 00 00 00       	cmp    eax,0xb6
    28b7:	0f 94 c0             	sete   al
    28ba:	5d                   	pop    rbp
    28bb:	c3                   	ret    

00000000000028bc <f9521409>:
    28bc:	f3 0f 1e fa          	endbr64 
    28c0:	55                   	push   rbp
    28c1:	48 89 e5             	mov    rbp,rsp
    28c4:	89 f8                	mov    eax,edi
    28c6:	88 45 fc             	mov    BYTE PTR [rbp-0x4],al
    28c9:	0f be 45 fc          	movsx  eax,BYTE PTR [rbp-0x4]
    28cd:	c1 e0 04             	shl    eax,0x4
    28d0:	0f b6 d0             	movzx  edx,al
    28d3:	0f b6 45 fc          	movzx  eax,BYTE PTR [rbp-0x4]
    28d7:	c0 f8 04             	sar    al,0x4
    28da:	0f be c0             	movsx  eax,al
    28dd:	01 d0                	add    eax,edx
    28df:	83 f8 33             	cmp    eax,0x33
    28e2:	0f 94 c0             	sete   al
    28e5:	5d                   	pop    rbp
    28e6:	c3                   	ret    

00000000000028e7 <f6147350>:
    28e7:	f3 0f 1e fa          	endbr64 
    28eb:	55                   	push   rbp
    28ec:	48 89 e5             	mov    rbp,rsp
    28ef:	89 f8                	mov    eax,edi
    28f1:	88 45 fc             	mov    BYTE PTR [rbp-0x4],al
    28f4:	0f be 45 fc          	movsx  eax,BYTE PTR [rbp-0x4]
    28f8:	c1 e0 04             	shl    eax,0x4
    28fb:	0f b6 d0             	movzx  edx,al
    28fe:	0f b6 45 fc          	movzx  eax,BYTE PTR [rbp-0x4]
    2902:	c0 f8 04             	sar    al,0x4
    2905:	0f be c0             	movsx  eax,al
    2908:	01 d0                	add    eax,edx
    290a:	3d f5 00 00 00       	cmp    eax,0xf5
    290f:	0f 94 c0             	sete   al
    2912:	5d                   	pop    rbp
    2913:	c3                   	ret    

0000000000002914 <f3296195>:
    2914:	f3 0f 1e fa          	endbr64 
    2918:	55                   	push   rbp
    2919:	48 89 e5             	mov    rbp,rsp
    291c:	89 f8                	mov    eax,edi
    291e:	88 45 fc             	mov    BYTE PTR [rbp-0x4],al
    2921:	0f be 45 fc          	movsx  eax,BYTE PTR [rbp-0x4]
    2925:	c1 e0 04             	shl    eax,0x4
    2928:	0f b6 d0             	movzx  edx,al
    292b:	0f b6 45 fc          	movzx  eax,BYTE PTR [rbp-0x4]
    292f:	c0 f8 04             	sar    al,0x4
    2932:	0f be c0             	movsx  eax,al
    2935:	01 d0                	add    eax,edx
    2937:	3d 97 00 00 00       	cmp    eax,0x97
    293c:	0f 94 c0             	sete   al
    293f:	5d                   	pop    rbp
    2940:	c3                   	ret    

0000000000002941 <f5547465>:
    2941:	f3 0f 1e fa          	endbr64 
    2945:	55                   	push   rbp
    2946:	48 89 e5             	mov    rbp,rsp
    2949:	89 f8                	mov    eax,edi
    294b:	88 45 fc             	mov    BYTE PTR [rbp-0x4],al
    294e:	0f be 45 fc          	movsx  eax,BYTE PTR [rbp-0x4]
    2952:	c1 e0 04             	shl    eax,0x4
    2955:	0f b6 d0             	movzx  edx,al
    2958:	0f b6 45 fc          	movzx  eax,BYTE PTR [rbp-0x4]
    295c:	c0 f8 04             	sar    al,0x4
    295f:	0f be c0             	movsx  eax,al
    2962:	01 d0                	add    eax,edx
    2964:	83 f8 03             	cmp    eax,0x3
    2967:	0f 94 c0             	sete   al
    296a:	5d                   	pop    rbp
    296b:	c3                   	ret    

000000000000296c <f3950848>:
    296c:	f3 0f 1e fa          	endbr64 
    2970:	55                   	push   rbp
    2971:	48 89 e5             	mov    rbp,rsp
    2974:	89 f8                	mov    eax,edi
    2976:	88 45 fc             	mov    BYTE PTR [rbp-0x4],al
    2979:	0f be 45 fc          	movsx  eax,BYTE PTR [rbp-0x4]
    297d:	c1 e0 04             	shl    eax,0x4
    2980:	0f b6 d0             	movzx  edx,al
    2983:	0f b6 45 fc          	movzx  eax,BYTE PTR [rbp-0x4]
    2987:	c0 f8 04             	sar    al,0x4
    298a:	0f be c0             	movsx  eax,al
    298d:	01 d0                	add    eax,edx
    298f:	83 f8 57             	cmp    eax,0x57
    2992:	0f 94 c0             	sete   al
    2995:	5d                   	pop    rbp
    2996:	c3                   	ret    

0000000000002997 <f8974270>:
    2997:	f3 0f 1e fa          	endbr64 
    299b:	55                   	push   rbp
    299c:	48 89 e5             	mov    rbp,rsp
    299f:	89 f8                	mov    eax,edi
    29a1:	88 45 fc             	mov    BYTE PTR [rbp-0x4],al
    29a4:	0f be 45 fc          	movsx  eax,BYTE PTR [rbp-0x4]
    29a8:	c1 e0 04             	shl    eax,0x4
    29ab:	0f b6 d0             	movzx  edx,al
    29ae:	0f b6 45 fc          	movzx  eax,BYTE PTR [rbp-0x4]
    29b2:	c0 f8 04             	sar    al,0x4
    29b5:	0f be c0             	movsx  eax,al
    29b8:	01 d0                	add    eax,edx
    29ba:	83 f8 27             	cmp    eax,0x27
    29bd:	0f 94 c0             	sete   al
    29c0:	5d                   	pop    rbp
    29c1:	c3                   	ret    

00000000000029c2 <f3371760>:
    29c2:	f3 0f 1e fa          	endbr64 
    29c6:	55                   	push   rbp
    29c7:	48 89 e5             	mov    rbp,rsp
    29ca:	89 f8                	mov    eax,edi
    29cc:	88 45 fc             	mov    BYTE PTR [rbp-0x4],al
    29cf:	0f be 45 fc          	movsx  eax,BYTE PTR [rbp-0x4]
    29d3:	c1 e0 04             	shl    eax,0x4
    29d6:	0f b6 d0             	movzx  edx,al
    29d9:	0f b6 45 fc          	movzx  eax,BYTE PTR [rbp-0x4]
    29dd:	c0 f8 04             	sar    al,0x4
    29e0:	0f be c0             	movsx  eax,al
    29e3:	01 d0                	add    eax,edx
    29e5:	3d f5 00 00 00       	cmp    eax,0xf5
    29ea:	0f 94 c0             	sete   al
    29ed:	5d                   	pop    rbp
    29ee:	c3                   	ret    

00000000000029ef <f9565003>:
    29ef:	f3 0f 1e fa          	endbr64 
    29f3:	55                   	push   rbp
    29f4:	48 89 e5             	mov    rbp,rsp
    29f7:	89 f8                	mov    eax,edi
    29f9:	88 45 fc             	mov    BYTE PTR [rbp-0x4],al
    29fc:	0f be 45 fc          	movsx  eax,BYTE PTR [rbp-0x4]
    2a00:	c1 e0 04             	shl    eax,0x4
    2a03:	0f b6 d0             	movzx  edx,al
    2a06:	0f b6 45 fc          	movzx  eax,BYTE PTR [rbp-0x4]
    2a0a:	c0 f8 04             	sar    al,0x4
    2a0d:	0f be c0             	movsx  eax,al
    2a10:	01 d0                	add    eax,edx
    2a12:	3d c6 00 00 00       	cmp    eax,0xc6
    2a17:	0f 94 c0             	sete   al
    2a1a:	5d                   	pop    rbp
    2a1b:	c3                   	ret    

0000000000002a1c <f3189640>:
    2a1c:	f3 0f 1e fa          	endbr64 
    2a20:	55                   	push   rbp
    2a21:	48 89 e5             	mov    rbp,rsp
    2a24:	89 f8                	mov    eax,edi
    2a26:	88 45 fc             	mov    BYTE PTR [rbp-0x4],al
    2a29:	0f be 45 fc          	movsx  eax,BYTE PTR [rbp-0x4]
    2a2d:	c1 e0 04             	shl    eax,0x4
    2a30:	0f b6 d0             	movzx  edx,al
    2a33:	0f b6 45 fc          	movzx  eax,BYTE PTR [rbp-0x4]
    2a37:	c0 f8 04             	sar    al,0x4
    2a3a:	0f be c0             	movsx  eax,al
    2a3d:	01 d0                	add    eax,edx
    2a3f:	83 f8 13             	cmp    eax,0x13
    2a42:	0f 94 c0             	sete   al
    2a45:	5d                   	pop    rbp
    2a46:	c3                   	ret    

0000000000002a47 <f3873488>:
    2a47:	f3 0f 1e fa          	endbr64 
    2a4b:	55                   	push   rbp
    2a4c:	48 89 e5             	mov    rbp,rsp
    2a4f:	89 f8                	mov    eax,edi
    2a51:	88 45 fc             	mov    BYTE PTR [rbp-0x4],al
    2a54:	0f be 45 fc          	movsx  eax,BYTE PTR [rbp-0x4]
    2a58:	c1 e0 04             	shl    eax,0x4
    2a5b:	0f b6 d0             	movzx  edx,al
    2a5e:	0f b6 45 fc          	movzx  eax,BYTE PTR [rbp-0x4]
    2a62:	c0 f8 04             	sar    al,0x4
    2a65:	0f be c0             	movsx  eax,al
    2a68:	01 d0                	add    eax,edx
    2a6a:	83 f8 66             	cmp    eax,0x66
    2a6d:	0f 94 c0             	sete   al
    2a70:	5d                   	pop    rbp
    2a71:	c3                   	ret    

0000000000002a72 <f9392038>:
    2a72:	f3 0f 1e fa          	endbr64 
    2a76:	55                   	push   rbp
    2a77:	48 89 e5             	mov    rbp,rsp
    2a7a:	89 f8                	mov    eax,edi
    2a7c:	88 45 fc             	mov    BYTE PTR [rbp-0x4],al
    2a7f:	0f be 45 fc          	movsx  eax,BYTE PTR [rbp-0x4]
    2a83:	c1 e0 04             	shl    eax,0x4
    2a86:	0f b6 d0             	movzx  edx,al
    2a89:	0f b6 45 fc          	movzx  eax,BYTE PTR [rbp-0x4]
    2a8d:	c0 f8 04             	sar    al,0x4
    2a90:	0f be c0             	movsx  eax,al
    2a93:	01 d0                	add    eax,edx
    2a95:	83 f8 33             	cmp    eax,0x33
    2a98:	0f 94 c0             	sete   al
    2a9b:	5d                   	pop    rbp
    2a9c:	c3                   	ret    

0000000000002a9d <f7515979>:
    2a9d:	f3 0f 1e fa          	endbr64 
    2aa1:	55                   	push   rbp
    2aa2:	48 89 e5             	mov    rbp,rsp
    2aa5:	89 f8                	mov    eax,edi
    2aa7:	88 45 fc             	mov    BYTE PTR [rbp-0x4],al
    2aaa:	0f be 45 fc          	movsx  eax,BYTE PTR [rbp-0x4]
    2aae:	c1 e0 04             	shl    eax,0x4
    2ab1:	0f b6 d0             	movzx  edx,al
    2ab4:	0f b6 45 fc          	movzx  eax,BYTE PTR [rbp-0x4]
    2ab8:	c0 f8 04             	sar    al,0x4
    2abb:	0f be c0             	movsx  eax,al
    2abe:	01 d0                	add    eax,edx
    2ac0:	3d f5 00 00 00       	cmp    eax,0xf5
    2ac5:	0f 94 c0             	sete   al
    2ac8:	5d                   	pop    rbp
    2ac9:	c3                   	ret    

0000000000002aca <f2754289>:
    2aca:	f3 0f 1e fa          	endbr64 
    2ace:	55                   	push   rbp
    2acf:	48 89 e5             	mov    rbp,rsp
    2ad2:	89 f8                	mov    eax,edi
    2ad4:	88 45 fc             	mov    BYTE PTR [rbp-0x4],al
    2ad7:	0f be 45 fc          	movsx  eax,BYTE PTR [rbp-0x4]
    2adb:	c1 e0 04             	shl    eax,0x4
    2ade:	0f b6 d0             	movzx  edx,al
    2ae1:	0f b6 45 fc          	movzx  eax,BYTE PTR [rbp-0x4]
    2ae5:	c0 f8 04             	sar    al,0x4
    2ae8:	0f be c0             	movsx  eax,al
    2aeb:	01 d0                	add    eax,edx
    2aed:	3d d6 00 00 00       	cmp    eax,0xd6
    2af2:	0f 94 c0             	sete   al
    2af5:	5d                   	pop    rbp
    2af6:	c3                   	ret    

0000000000002af7 <f2916766>:
    2af7:	f3 0f 1e fa          	endbr64 
    2afb:	55                   	push   rbp
    2afc:	48 89 e5             	mov    rbp,rsp
    2aff:	89 f8                	mov    eax,edi
    2b01:	88 45 fc             	mov    BYTE PTR [rbp-0x4],al
    2b04:	0f be 45 fc          	movsx  eax,BYTE PTR [rbp-0x4]
    2b08:	c1 e0 04             	shl    eax,0x4
    2b0b:	0f b6 d0             	movzx  edx,al
    2b0e:	0f b6 45 fc          	movzx  eax,BYTE PTR [rbp-0x4]
    2b12:	c0 f8 04             	sar    al,0x4
    2b15:	0f be c0             	movsx  eax,al
    2b18:	01 d0                	add    eax,edx
    2b1a:	83 f8 57             	cmp    eax,0x57
    2b1d:	0f 94 c0             	sete   al
    2b20:	5d                   	pop    rbp
    2b21:	c3                   	ret    

0000000000002b22 <f3574708>:
    2b22:	f3 0f 1e fa          	endbr64 
    2b26:	55                   	push   rbp
    2b27:	48 89 e5             	mov    rbp,rsp
    2b2a:	89 f8                	mov    eax,edi
    2b2c:	88 45 fc             	mov    BYTE PTR [rbp-0x4],al
    2b2f:	0f be 45 fc          	movsx  eax,BYTE PTR [rbp-0x4]
    2b33:	c1 e0 04             	shl    eax,0x4
    2b36:	0f b6 d0             	movzx  edx,al
    2b39:	0f b6 45 fc          	movzx  eax,BYTE PTR [rbp-0x4]
    2b3d:	c0 f8 04             	sar    al,0x4
    2b40:	0f be c0             	movsx  eax,al
    2b43:	01 d0                	add    eax,edx
    2b45:	83 f8 36             	cmp    eax,0x36
    2b48:	0f 94 c0             	sete   al
    2b4b:	5d                   	pop    rbp
    2b4c:	c3                   	ret    

0000000000002b4d <f5319150>:
    2b4d:	f3 0f 1e fa          	endbr64 
    2b51:	55                   	push   rbp
    2b52:	48 89 e5             	mov    rbp,rsp
    2b55:	89 f8                	mov    eax,edi
    2b57:	88 45 fc             	mov    BYTE PTR [rbp-0x4],al
    2b5a:	0f be 45 fc          	movsx  eax,BYTE PTR [rbp-0x4]
    2b5e:	c1 e0 04             	shl    eax,0x4
    2b61:	0f b6 d0             	movzx  edx,al
    2b64:	0f b6 45 fc          	movzx  eax,BYTE PTR [rbp-0x4]
    2b68:	c0 f8 04             	sar    al,0x4
    2b6b:	0f be c0             	movsx  eax,al
    2b6e:	01 d0                	add    eax,edx
    2b70:	3d 86 00 00 00       	cmp    eax,0x86
    2b75:	0f 94 c0             	sete   al
    2b78:	5d                   	pop    rbp
    2b79:	c3                   	ret    

0000000000002b7a <f10076>:
    2b7a:	f3 0f 1e fa          	endbr64 
    2b7e:	55                   	push   rbp
    2b7f:	48 89 e5             	mov    rbp,rsp
    2b82:	89 f8                	mov    eax,edi
    2b84:	88 45 fc             	mov    BYTE PTR [rbp-0x4],al
    2b87:	0f be 45 fc          	movsx  eax,BYTE PTR [rbp-0x4]
    2b8b:	c1 e0 04             	shl    eax,0x4
    2b8e:	0f b6 d0             	movzx  edx,al
    2b91:	0f b6 45 fc          	movzx  eax,BYTE PTR [rbp-0x4]
    2b95:	c0 f8 04             	sar    al,0x4
    2b98:	0f be c0             	movsx  eax,al
    2b9b:	01 d0                	add    eax,edx
    2b9d:	3d f5 00 00 00       	cmp    eax,0xf5
    2ba2:	0f 94 c0             	sete   al
    2ba5:	5d                   	pop    rbp
    2ba6:	c3                   	ret    

0000000000002ba7 <f7175572>:
    2ba7:	f3 0f 1e fa          	endbr64 
    2bab:	55                   	push   rbp
    2bac:	48 89 e5             	mov    rbp,rsp
    2baf:	89 f8                	mov    eax,edi
    2bb1:	88 45 fc             	mov    BYTE PTR [rbp-0x4],al
    2bb4:	0f be 45 fc          	movsx  eax,BYTE PTR [rbp-0x4]
    2bb8:	c1 e0 04             	shl    eax,0x4
    2bbb:	0f b6 d0             	movzx  edx,al
    2bbe:	0f b6 45 fc          	movzx  eax,BYTE PTR [rbp-0x4]
    2bc2:	c0 f8 04             	sar    al,0x4
    2bc5:	0f be c0             	movsx  eax,al
    2bc8:	01 d0                	add    eax,edx
    2bca:	83 f8 56             	cmp    eax,0x56
    2bcd:	0f 94 c0             	sete   al
    2bd0:	5d                   	pop    rbp
    2bd1:	c3                   	ret    

0000000000002bd2 <f2614917>:
    2bd2:	f3 0f 1e fa          	endbr64 
    2bd6:	55                   	push   rbp
    2bd7:	48 89 e5             	mov    rbp,rsp
    2bda:	89 f8                	mov    eax,edi
    2bdc:	88 45 fc             	mov    BYTE PTR [rbp-0x4],al
    2bdf:	0f be 45 fc          	movsx  eax,BYTE PTR [rbp-0x4]
    2be3:	c1 e0 04             	shl    eax,0x4
    2be6:	0f b6 d0             	movzx  edx,al
    2be9:	0f b6 45 fc          	movzx  eax,BYTE PTR [rbp-0x4]
    2bed:	c0 f8 04             	sar    al,0x4
    2bf0:	0f be c0             	movsx  eax,al
    2bf3:	01 d0                	add    eax,edx
    2bf5:	83 f8 43             	cmp    eax,0x43
    2bf8:	0f 94 c0             	sete   al
    2bfb:	5d                   	pop    rbp
    2bfc:	c3                   	ret    

0000000000002bfd <f1787361>:
    2bfd:	f3 0f 1e fa          	endbr64 
    2c01:	55                   	push   rbp
    2c02:	48 89 e5             	mov    rbp,rsp
    2c05:	89 f8                	mov    eax,edi
    2c07:	88 45 fc             	mov    BYTE PTR [rbp-0x4],al
    2c0a:	0f be 45 fc          	movsx  eax,BYTE PTR [rbp-0x4]
    2c0e:	c1 e0 04             	shl    eax,0x4
    2c11:	0f b6 d0             	movzx  edx,al
    2c14:	0f b6 45 fc          	movzx  eax,BYTE PTR [rbp-0x4]
    2c18:	c0 f8 04             	sar    al,0x4
    2c1b:	0f be c0             	movsx  eax,al
    2c1e:	01 d0                	add    eax,edx
    2c20:	83 f8 37             	cmp    eax,0x37
    2c23:	0f 94 c0             	sete   al
    2c26:	5d                   	pop    rbp
    2c27:	c3                   	ret    

0000000000002c28 <f4506152>:
    2c28:	f3 0f 1e fa          	endbr64 
    2c2c:	55                   	push   rbp
    2c2d:	48 89 e5             	mov    rbp,rsp
    2c30:	89 f8                	mov    eax,edi
    2c32:	88 45 fc             	mov    BYTE PTR [rbp-0x4],al
    2c35:	0f be 45 fc          	movsx  eax,BYTE PTR [rbp-0x4]
    2c39:	c1 e0 04             	shl    eax,0x4
    2c3c:	0f b6 d0             	movzx  edx,al
    2c3f:	0f b6 45 fc          	movzx  eax,BYTE PTR [rbp-0x4]
    2c43:	c0 f8 04             	sar    al,0x4
    2c46:	0f be c0             	movsx  eax,al
    2c49:	01 d0                	add    eax,edx
    2c4b:	83 f8 13             	cmp    eax,0x13
    2c4e:	0f 94 c0             	sete   al
    2c51:	5d                   	pop    rbp
    2c52:	c3                   	ret    

0000000000002c53 <f8769072>:
    2c53:	f3 0f 1e fa          	endbr64 
    2c57:	55                   	push   rbp
    2c58:	48 89 e5             	mov    rbp,rsp
    2c5b:	89 f8                	mov    eax,edi
    2c5d:	88 45 fc             	mov    BYTE PTR [rbp-0x4],al
    2c60:	0f be 45 fc          	movsx  eax,BYTE PTR [rbp-0x4]
    2c64:	c1 e0 04             	shl    eax,0x4
    2c67:	0f b6 d0             	movzx  edx,al
    2c6a:	0f b6 45 fc          	movzx  eax,BYTE PTR [rbp-0x4]
    2c6e:	c0 f8 04             	sar    al,0x4
    2c71:	0f be c0             	movsx  eax,al
    2c74:	01 d0                	add    eax,edx
    2c76:	83 f8 33             	cmp    eax,0x33
    2c79:	0f 94 c0             	sete   al
    2c7c:	5d                   	pop    rbp
    2c7d:	c3                   	ret    

0000000000002c7e <f7138486>:
    2c7e:	f3 0f 1e fa          	endbr64 
    2c82:	55                   	push   rbp
    2c83:	48 89 e5             	mov    rbp,rsp
    2c86:	89 f8                	mov    eax,edi
    2c88:	88 45 fc             	mov    BYTE PTR [rbp-0x4],al
    2c8b:	0f be 45 fc          	movsx  eax,BYTE PTR [rbp-0x4]
    2c8f:	c1 e0 04             	shl    eax,0x4
    2c92:	0f b6 d0             	movzx  edx,al
    2c95:	0f b6 45 fc          	movzx  eax,BYTE PTR [rbp-0x4]
    2c99:	c0 f8 04             	sar    al,0x4
    2c9c:	0f be c0             	movsx  eax,al
    2c9f:	01 d0                	add    eax,edx
    2ca1:	83 f8 27             	cmp    eax,0x27
    2ca4:	0f 94 c0             	sete   al
    2ca7:	5d                   	pop    rbp
    2ca8:	c3                   	ret    

0000000000002ca9 <f8239086>:
    2ca9:	f3 0f 1e fa          	endbr64 
    2cad:	55                   	push   rbp
    2cae:	48 89 e5             	mov    rbp,rsp
    2cb1:	89 f8                	mov    eax,edi
    2cb3:	88 45 fc             	mov    BYTE PTR [rbp-0x4],al
    2cb6:	0f be 45 fc          	movsx  eax,BYTE PTR [rbp-0x4]
    2cba:	c1 e0 04             	shl    eax,0x4
    2cbd:	0f b6 d0             	movzx  edx,al
    2cc0:	0f b6 45 fc          	movzx  eax,BYTE PTR [rbp-0x4]
    2cc4:	c0 f8 04             	sar    al,0x4
    2cc7:	0f be c0             	movsx  eax,al
    2cca:	01 d0                	add    eax,edx
    2ccc:	3d e2 00 00 00       	cmp    eax,0xe2
    2cd1:	0f 94 c0             	sete   al
    2cd4:	5d                   	pop    rbp
    2cd5:	c3                   	ret    

0000000000002cd6 <f4507173>:
    2cd6:	f3 0f 1e fa          	endbr64 
    2cda:	55                   	push   rbp
    2cdb:	48 89 e5             	mov    rbp,rsp
    2cde:	89 f8                	mov    eax,edi
    2ce0:	88 45 fc             	mov    BYTE PTR [rbp-0x4],al
    2ce3:	0f be 45 fc          	movsx  eax,BYTE PTR [rbp-0x4]
    2ce7:	c1 e0 04             	shl    eax,0x4
    2cea:	0f b6 d0             	movzx  edx,al
    2ced:	0f b6 45 fc          	movzx  eax,BYTE PTR [rbp-0x4]
    2cf1:	c0 f8 04             	sar    al,0x4
    2cf4:	0f be c0             	movsx  eax,al
    2cf7:	01 d0                	add    eax,edx
    2cf9:	83 f8 34             	cmp    eax,0x34
    2cfc:	0f 94 c0             	sete   al
    2cff:	5d                   	pop    rbp
    2d00:	c3                   	ret    

0000000000002d01 <f3890123>:
    2d01:	f3 0f 1e fa          	endbr64 
    2d05:	55                   	push   rbp
    2d06:	48 89 e5             	mov    rbp,rsp
    2d09:	89 f8                	mov    eax,edi
    2d0b:	88 45 fc             	mov    BYTE PTR [rbp-0x4],al
    2d0e:	0f be 45 fc          	movsx  eax,BYTE PTR [rbp-0x4]
    2d12:	c1 e0 04             	shl    eax,0x4
    2d15:	0f b6 d0             	movzx  edx,al
    2d18:	0f b6 45 fc          	movzx  eax,BYTE PTR [rbp-0x4]
    2d1c:	c0 f8 04             	sar    al,0x4
    2d1f:	0f be c0             	movsx  eax,al
    2d22:	01 d0                	add    eax,edx
    2d24:	83 f8 03             	cmp    eax,0x3
    2d27:	0f 94 c0             	sete   al
    2d2a:	5d                   	pop    rbp
    2d2b:	c3                   	ret    

0000000000002d2c <f5431205>:
    2d2c:	f3 0f 1e fa          	endbr64 
    2d30:	55                   	push   rbp
    2d31:	48 89 e5             	mov    rbp,rsp
    2d34:	89 f8                	mov    eax,edi
    2d36:	88 45 fc             	mov    BYTE PTR [rbp-0x4],al
    2d39:	0f be 45 fc          	movsx  eax,BYTE PTR [rbp-0x4]
    2d3d:	c1 e0 04             	shl    eax,0x4
    2d40:	0f b6 d0             	movzx  edx,al
    2d43:	0f b6 45 fc          	movzx  eax,BYTE PTR [rbp-0x4]
    2d47:	c0 f8 04             	sar    al,0x4
    2d4a:	0f be c0             	movsx  eax,al
    2d4d:	01 d0                	add    eax,edx
    2d4f:	3d e6 00 00 00       	cmp    eax,0xe6
    2d54:	0f 94 c0             	sete   al
    2d57:	5d                   	pop    rbp
    2d58:	c3                   	ret    

0000000000002d59 <f8149070>:
    2d59:	f3 0f 1e fa          	endbr64 
    2d5d:	55                   	push   rbp
    2d5e:	48 89 e5             	mov    rbp,rsp
    2d61:	89 f8                	mov    eax,edi
    2d63:	88 45 fc             	mov    BYTE PTR [rbp-0x4],al
    2d66:	0f be 45 fc          	movsx  eax,BYTE PTR [rbp-0x4]
    2d6a:	c1 e0 04             	shl    eax,0x4
    2d6d:	0f b6 d0             	movzx  edx,al
    2d70:	0f b6 45 fc          	movzx  eax,BYTE PTR [rbp-0x4]
    2d74:	c0 f8 04             	sar    al,0x4
    2d77:	0f be c0             	movsx  eax,al
    2d7a:	01 d0                	add    eax,edx
    2d7c:	83 f8 76             	cmp    eax,0x76
    2d7f:	0f 94 c0             	sete   al
    2d82:	5d                   	pop    rbp
    2d83:	c3                   	ret    

0000000000002d84 <f9439381>:
    2d84:	f3 0f 1e fa          	endbr64 
    2d88:	55                   	push   rbp
    2d89:	48 89 e5             	mov    rbp,rsp
    2d8c:	89 f8                	mov    eax,edi
    2d8e:	88 45 fc             	mov    BYTE PTR [rbp-0x4],al
    2d91:	0f be 45 fc          	movsx  eax,BYTE PTR [rbp-0x4]
    2d95:	c1 e0 04             	shl    eax,0x4
    2d98:	0f b6 d0             	movzx  edx,al
    2d9b:	0f b6 45 fc          	movzx  eax,BYTE PTR [rbp-0x4]
    2d9f:	c0 f8 04             	sar    al,0x4
    2da2:	0f be c0             	movsx  eax,al
    2da5:	01 d0                	add    eax,edx
    2da7:	83 f8 27             	cmp    eax,0x27
    2daa:	0f 94 c0             	sete   al
    2dad:	5d                   	pop    rbp
    2dae:	c3                   	ret    

0000000000002daf <f9055518>:
    2daf:	f3 0f 1e fa          	endbr64 
    2db3:	55                   	push   rbp
    2db4:	48 89 e5             	mov    rbp,rsp
    2db7:	89 f8                	mov    eax,edi
    2db9:	88 45 fc             	mov    BYTE PTR [rbp-0x4],al
    2dbc:	0f be 45 fc          	movsx  eax,BYTE PTR [rbp-0x4]
    2dc0:	c1 e0 04             	shl    eax,0x4
    2dc3:	0f b6 d0             	movzx  edx,al
    2dc6:	0f b6 45 fc          	movzx  eax,BYTE PTR [rbp-0x4]
    2dca:	c0 f8 04             	sar    al,0x4
    2dcd:	0f be c0             	movsx  eax,al
    2dd0:	01 d0                	add    eax,edx
    2dd2:	83 f8 43             	cmp    eax,0x43
    2dd5:	0f 94 c0             	sete   al
    2dd8:	5d                   	pop    rbp
    2dd9:	c3                   	ret    

0000000000002dda <f9075068>:
    2dda:	f3 0f 1e fa          	endbr64 
    2dde:	55                   	push   rbp
    2ddf:	48 89 e5             	mov    rbp,rsp
    2de2:	89 f8                	mov    eax,edi
    2de4:	88 45 fc             	mov    BYTE PTR [rbp-0x4],al
    2de7:	0f be 45 fc          	movsx  eax,BYTE PTR [rbp-0x4]
    2deb:	c1 e0 04             	shl    eax,0x4
    2dee:	0f b6 d0             	movzx  edx,al
    2df1:	0f b6 45 fc          	movzx  eax,BYTE PTR [rbp-0x4]
    2df5:	c0 f8 04             	sar    al,0x4
    2df8:	0f be c0             	movsx  eax,al
    2dfb:	01 d0                	add    eax,edx
    2dfd:	83 f8 47             	cmp    eax,0x47
    2e00:	0f 94 c0             	sete   al
    2e03:	5d                   	pop    rbp
    2e04:	c3                   	ret    

0000000000002e05 <f9635223>:
    2e05:	f3 0f 1e fa          	endbr64 
    2e09:	55                   	push   rbp
    2e0a:	48 89 e5             	mov    rbp,rsp
    2e0d:	89 f8                	mov    eax,edi
    2e0f:	88 45 fc             	mov    BYTE PTR [rbp-0x4],al
    2e12:	0f be 45 fc          	movsx  eax,BYTE PTR [rbp-0x4]
    2e16:	c1 e0 04             	shl    eax,0x4
    2e19:	0f b6 d0             	movzx  edx,al
    2e1c:	0f b6 45 fc          	movzx  eax,BYTE PTR [rbp-0x4]
    2e20:	c0 f8 04             	sar    al,0x4
    2e23:	0f be c0             	movsx  eax,al
    2e26:	01 d0                	add    eax,edx
    2e28:	83 f8 37             	cmp    eax,0x37
    2e2b:	0f 94 c0             	sete   al
    2e2e:	5d                   	pop    rbp
    2e2f:	c3                   	ret    

0000000000002e30 <f9449880>:
    2e30:	f3 0f 1e fa          	endbr64 
    2e34:	55                   	push   rbp
    2e35:	48 89 e5             	mov    rbp,rsp
    2e38:	89 f8                	mov    eax,edi
    2e3a:	88 45 fc             	mov    BYTE PTR [rbp-0x4],al
    2e3d:	0f be 45 fc          	movsx  eax,BYTE PTR [rbp-0x4]
    2e41:	c1 e0 04             	shl    eax,0x4
    2e44:	0f b6 d0             	movzx  edx,al
    2e47:	0f b6 45 fc          	movzx  eax,BYTE PTR [rbp-0x4]
    2e4b:	c0 f8 04             	sar    al,0x4
    2e4e:	0f be c0             	movsx  eax,al
    2e51:	01 d0                	add    eax,edx
    2e53:	3d f5 00 00 00       	cmp    eax,0xf5
    2e58:	0f 94 c0             	sete   al
    2e5b:	5d                   	pop    rbp
    2e5c:	c3                   	ret    

0000000000002e5d <f9273721>:
    2e5d:	f3 0f 1e fa          	endbr64 
    2e61:	55                   	push   rbp
    2e62:	48 89 e5             	mov    rbp,rsp
    2e65:	89 f8                	mov    eax,edi
    2e67:	88 45 fc             	mov    BYTE PTR [rbp-0x4],al
    2e6a:	0f be 45 fc          	movsx  eax,BYTE PTR [rbp-0x4]
    2e6e:	c1 e0 04             	shl    eax,0x4
    2e71:	0f b6 d0             	movzx  edx,al
    2e74:	0f b6 45 fc          	movzx  eax,BYTE PTR [rbp-0x4]
    2e78:	c0 f8 04             	sar    al,0x4
    2e7b:	0f be c0             	movsx  eax,al
    2e7e:	01 d0                	add    eax,edx
    2e80:	83 f8 66             	cmp    eax,0x66
    2e83:	0f 94 c0             	sete   al
    2e86:	5d                   	pop    rbp
    2e87:	c3                   	ret    

0000000000002e88 <f4577902>:
    2e88:	f3 0f 1e fa          	endbr64 
    2e8c:	55                   	push   rbp
    2e8d:	48 89 e5             	mov    rbp,rsp
    2e90:	89 f8                	mov    eax,edi
    2e92:	88 45 fc             	mov    BYTE PTR [rbp-0x4],al
    2e95:	0f be 45 fc          	movsx  eax,BYTE PTR [rbp-0x4]
    2e99:	c1 e0 04             	shl    eax,0x4
    2e9c:	0f b6 d0             	movzx  edx,al
    2e9f:	0f b6 45 fc          	movzx  eax,BYTE PTR [rbp-0x4]
    2ea3:	c0 f8 04             	sar    al,0x4
    2ea6:	0f be c0             	movsx  eax,al
    2ea9:	01 d0                	add    eax,edx
    2eab:	83 f8 03             	cmp    eax,0x3
    2eae:	0f 94 c0             	sete   al
    2eb1:	5d                   	pop    rbp
    2eb2:	c3                   	ret    

0000000000002eb3 <f5841651>:
    2eb3:	f3 0f 1e fa          	endbr64 
    2eb7:	55                   	push   rbp
    2eb8:	48 89 e5             	mov    rbp,rsp
    2ebb:	89 f8                	mov    eax,edi
    2ebd:	88 45 fc             	mov    BYTE PTR [rbp-0x4],al
    2ec0:	0f be 45 fc          	movsx  eax,BYTE PTR [rbp-0x4]
    2ec4:	c1 e0 04             	shl    eax,0x4
    2ec7:	0f b6 d0             	movzx  edx,al
    2eca:	0f b6 45 fc          	movzx  eax,BYTE PTR [rbp-0x4]
    2ece:	c0 f8 04             	sar    al,0x4
    2ed1:	0f be c0             	movsx  eax,al
    2ed4:	01 d0                	add    eax,edx
    2ed6:	83 f8 27             	cmp    eax,0x27
    2ed9:	0f 94 c0             	sete   al
    2edc:	5d                   	pop    rbp
    2edd:	c3                   	ret    

0000000000002ede <f5111051>:
    2ede:	f3 0f 1e fa          	endbr64 
    2ee2:	55                   	push   rbp
    2ee3:	48 89 e5             	mov    rbp,rsp
    2ee6:	89 f8                	mov    eax,edi
    2ee8:	88 45 fc             	mov    BYTE PTR [rbp-0x4],al
    2eeb:	0f be 45 fc          	movsx  eax,BYTE PTR [rbp-0x4]
    2eef:	c1 e0 04             	shl    eax,0x4
    2ef2:	0f b6 d0             	movzx  edx,al
    2ef5:	0f b6 45 fc          	movzx  eax,BYTE PTR [rbp-0x4]
    2ef9:	c0 f8 04             	sar    al,0x4
    2efc:	0f be c0             	movsx  eax,al
    2eff:	01 d0                	add    eax,edx
    2f01:	3d f5 00 00 00       	cmp    eax,0xf5
    2f06:	0f 94 c0             	sete   al
    2f09:	5d                   	pop    rbp
    2f0a:	c3                   	ret    

0000000000002f0b <f47276>:
    2f0b:	f3 0f 1e fa          	endbr64 
    2f0f:	55                   	push   rbp
    2f10:	48 89 e5             	mov    rbp,rsp
    2f13:	89 f8                	mov    eax,edi
    2f15:	88 45 fc             	mov    BYTE PTR [rbp-0x4],al
    2f18:	0f be 45 fc          	movsx  eax,BYTE PTR [rbp-0x4]
    2f1c:	c1 e0 04             	shl    eax,0x4
    2f1f:	0f b6 d0             	movzx  edx,al
    2f22:	0f b6 45 fc          	movzx  eax,BYTE PTR [rbp-0x4]
    2f26:	c0 f8 04             	sar    al,0x4
    2f29:	0f be c0             	movsx  eax,al
    2f2c:	01 d0                	add    eax,edx
    2f2e:	83 f8 37             	cmp    eax,0x37
    2f31:	0f 94 c0             	sete   al
    2f34:	5d                   	pop    rbp
    2f35:	c3                   	ret    

0000000000002f36 <f6350455>:
    2f36:	f3 0f 1e fa          	endbr64 
    2f3a:	55                   	push   rbp
    2f3b:	48 89 e5             	mov    rbp,rsp
    2f3e:	89 f8                	mov    eax,edi
    2f40:	88 45 fc             	mov    BYTE PTR [rbp-0x4],al
    2f43:	0f be 45 fc          	movsx  eax,BYTE PTR [rbp-0x4]
    2f47:	c1 e0 04             	shl    eax,0x4
    2f4a:	0f b6 d0             	movzx  edx,al
    2f4d:	0f b6 45 fc          	movzx  eax,BYTE PTR [rbp-0x4]
    2f51:	c0 f8 04             	sar    al,0x4
    2f54:	0f be c0             	movsx  eax,al
    2f57:	01 d0                	add    eax,edx
    2f59:	83 f8 03             	cmp    eax,0x3
    2f5c:	0f 94 c0             	sete   al
    2f5f:	5d                   	pop    rbp
    2f60:	c3                   	ret    

0000000000002f61 <f2402377>:
    2f61:	f3 0f 1e fa          	endbr64 
    2f65:	55                   	push   rbp
    2f66:	48 89 e5             	mov    rbp,rsp
    2f69:	89 f8                	mov    eax,edi
    2f6b:	88 45 fc             	mov    BYTE PTR [rbp-0x4],al
    2f6e:	0f be 45 fc          	movsx  eax,BYTE PTR [rbp-0x4]
    2f72:	c1 e0 04             	shl    eax,0x4
    2f75:	0f b6 d0             	movzx  edx,al
    2f78:	0f b6 45 fc          	movzx  eax,BYTE PTR [rbp-0x4]
    2f7c:	c0 f8 04             	sar    al,0x4
    2f7f:	0f be c0             	movsx  eax,al
    2f82:	01 d0                	add    eax,edx
    2f84:	3d c6 00 00 00       	cmp    eax,0xc6
    2f89:	0f 94 c0             	sete   al
    2f8c:	5d                   	pop    rbp
    2f8d:	c3                   	ret    

0000000000002f8e <f8761847>:
    2f8e:	f3 0f 1e fa          	endbr64 
    2f92:	55                   	push   rbp
    2f93:	48 89 e5             	mov    rbp,rsp
    2f96:	89 f8                	mov    eax,edi
    2f98:	88 45 fc             	mov    BYTE PTR [rbp-0x4],al
    2f9b:	0f be 45 fc          	movsx  eax,BYTE PTR [rbp-0x4]
    2f9f:	c1 e0 04             	shl    eax,0x4
    2fa2:	0f b6 d0             	movzx  edx,al
    2fa5:	0f b6 45 fc          	movzx  eax,BYTE PTR [rbp-0x4]
    2fa9:	c0 f8 04             	sar    al,0x4
    2fac:	0f be c0             	movsx  eax,al
    2faf:	01 d0                	add    eax,edx
    2fb1:	83 f8 67             	cmp    eax,0x67
    2fb4:	0f 94 c0             	sete   al
    2fb7:	5d                   	pop    rbp
    2fb8:	c3                   	ret    

0000000000002fb9 <f1849991>:
    2fb9:	f3 0f 1e fa          	endbr64 
    2fbd:	55                   	push   rbp
    2fbe:	48 89 e5             	mov    rbp,rsp
    2fc1:	89 f8                	mov    eax,edi
    2fc3:	88 45 fc             	mov    BYTE PTR [rbp-0x4],al
    2fc6:	0f be 45 fc          	movsx  eax,BYTE PTR [rbp-0x4]
    2fca:	c1 e0 04             	shl    eax,0x4
    2fcd:	0f b6 d0             	movzx  edx,al
    2fd0:	0f b6 45 fc          	movzx  eax,BYTE PTR [rbp-0x4]
    2fd4:	c0 f8 04             	sar    al,0x4
    2fd7:	0f be c0             	movsx  eax,al
    2fda:	01 d0                	add    eax,edx
    2fdc:	83 f8 13             	cmp    eax,0x13
    2fdf:	0f 94 c0             	sete   al
    2fe2:	5d                   	pop    rbp
    2fe3:	c3                   	ret    

0000000000002fe4 <f9094552>:
    2fe4:	f3 0f 1e fa          	endbr64 
    2fe8:	55                   	push   rbp
    2fe9:	48 89 e5             	mov    rbp,rsp
    2fec:	89 f8                	mov    eax,edi
    2fee:	88 45 fc             	mov    BYTE PTR [rbp-0x4],al
    2ff1:	0f be 45 fc          	movsx  eax,BYTE PTR [rbp-0x4]
    2ff5:	c1 e0 04             	shl    eax,0x4
    2ff8:	0f b6 d0             	movzx  edx,al
    2ffb:	0f b6 45 fc          	movzx  eax,BYTE PTR [rbp-0x4]
    2fff:	c0 f8 04             	sar    al,0x4
    3002:	0f be c0             	movsx  eax,al
    3005:	01 d0                	add    eax,edx
    3007:	3d 96 00 00 00       	cmp    eax,0x96
    300c:	0f 94 c0             	sete   al
    300f:	5d                   	pop    rbp
    3010:	c3                   	ret    

0000000000003011 <f217736>:
    3011:	f3 0f 1e fa          	endbr64 
    3015:	55                   	push   rbp
    3016:	48 89 e5             	mov    rbp,rsp
    3019:	89 f8                	mov    eax,edi
    301b:	88 45 fc             	mov    BYTE PTR [rbp-0x4],al
    301e:	0f be 45 fc          	movsx  eax,BYTE PTR [rbp-0x4]
    3022:	c1 e0 04             	shl    eax,0x4
    3025:	0f b6 d0             	movzx  edx,al
    3028:	0f b6 45 fc          	movzx  eax,BYTE PTR [rbp-0x4]
    302c:	c0 f8 04             	sar    al,0x4
    302f:	0f be c0             	movsx  eax,al
    3032:	01 d0                	add    eax,edx
    3034:	3d e6 00 00 00       	cmp    eax,0xe6
    3039:	0f 94 c0             	sete   al
    303c:	5d                   	pop    rbp
    303d:	c3                   	ret    

000000000000303e <f306999>:
    303e:	f3 0f 1e fa          	endbr64 
    3042:	55                   	push   rbp
    3043:	48 89 e5             	mov    rbp,rsp
    3046:	89 f8                	mov    eax,edi
    3048:	88 45 fc             	mov    BYTE PTR [rbp-0x4],al
    304b:	0f be 45 fc          	movsx  eax,BYTE PTR [rbp-0x4]
    304f:	c1 e0 04             	shl    eax,0x4
    3052:	0f b6 d0             	movzx  edx,al
    3055:	0f b6 45 fc          	movzx  eax,BYTE PTR [rbp-0x4]
    3059:	c0 f8 04             	sar    al,0x4
    305c:	0f be c0             	movsx  eax,al
    305f:	01 d0                	add    eax,edx
    3061:	3d 93 00 00 00       	cmp    eax,0x93
    3066:	0f 94 c0             	sete   al
    3069:	5d                   	pop    rbp
    306a:	c3                   	ret    

000000000000306b <f7863001>:
    306b:	f3 0f 1e fa          	endbr64 
    306f:	55                   	push   rbp
    3070:	48 89 e5             	mov    rbp,rsp
    3073:	89 f8                	mov    eax,edi
    3075:	88 45 fc             	mov    BYTE PTR [rbp-0x4],al
    3078:	0f be 45 fc          	movsx  eax,BYTE PTR [rbp-0x4]
    307c:	c1 e0 04             	shl    eax,0x4
    307f:	0f b6 d0             	movzx  edx,al
    3082:	0f b6 45 fc          	movzx  eax,BYTE PTR [rbp-0x4]
    3086:	c0 f8 04             	sar    al,0x4
    3089:	0f be c0             	movsx  eax,al
    308c:	01 d0                	add    eax,edx
    308e:	3d f5 00 00 00       	cmp    eax,0xf5
    3093:	0f 94 c0             	sete   al
    3096:	5d                   	pop    rbp
    3097:	c3                   	ret    

0000000000003098 <f3462476>:
    3098:	f3 0f 1e fa          	endbr64 
    309c:	55                   	push   rbp
    309d:	48 89 e5             	mov    rbp,rsp
    30a0:	89 f8                	mov    eax,edi
    30a2:	88 45 fc             	mov    BYTE PTR [rbp-0x4],al
    30a5:	0f be 45 fc          	movsx  eax,BYTE PTR [rbp-0x4]
    30a9:	c1 e0 04             	shl    eax,0x4
    30ac:	0f b6 d0             	movzx  edx,al
    30af:	0f b6 45 fc          	movzx  eax,BYTE PTR [rbp-0x4]
    30b3:	c0 f8 04             	sar    al,0x4
    30b6:	0f be c0             	movsx  eax,al
    30b9:	01 d0                	add    eax,edx
    30bb:	83 f8 47             	cmp    eax,0x47
    30be:	0f 94 c0             	sete   al
    30c1:	5d                   	pop    rbp
    30c2:	c3                   	ret    

00000000000030c3 <f2419198>:
    30c3:	f3 0f 1e fa          	endbr64 
    30c7:	55                   	push   rbp
    30c8:	48 89 e5             	mov    rbp,rsp
    30cb:	89 f8                	mov    eax,edi
    30cd:	88 45 fc             	mov    BYTE PTR [rbp-0x4],al
    30d0:	0f be 45 fc          	movsx  eax,BYTE PTR [rbp-0x4]
    30d4:	c1 e0 04             	shl    eax,0x4
    30d7:	0f b6 d0             	movzx  edx,al
    30da:	0f b6 45 fc          	movzx  eax,BYTE PTR [rbp-0x4]
    30de:	c0 f8 04             	sar    al,0x4
    30e1:	0f be c0             	movsx  eax,al
    30e4:	01 d0                	add    eax,edx
    30e6:	3d 86 00 00 00       	cmp    eax,0x86
    30eb:	0f 94 c0             	sete   al
    30ee:	5d                   	pop    rbp
    30ef:	c3                   	ret    

00000000000030f0 <f846584>:
    30f0:	f3 0f 1e fa          	endbr64 
    30f4:	55                   	push   rbp
    30f5:	48 89 e5             	mov    rbp,rsp
    30f8:	89 f8                	mov    eax,edi
    30fa:	88 45 fc             	mov    BYTE PTR [rbp-0x4],al
    30fd:	0f be 45 fc          	movsx  eax,BYTE PTR [rbp-0x4]
    3101:	c1 e0 04             	shl    eax,0x4
    3104:	0f b6 d0             	movzx  edx,al
    3107:	0f b6 45 fc          	movzx  eax,BYTE PTR [rbp-0x4]
    310b:	c0 f8 04             	sar    al,0x4
    310e:	0f be c0             	movsx  eax,al
    3111:	01 d0                	add    eax,edx
    3113:	83 f8 33             	cmp    eax,0x33
    3116:	0f 94 c0             	sete   al
    3119:	5d                   	pop    rbp
    311a:	c3                   	ret    

000000000000311b <f9397951>:
    311b:	f3 0f 1e fa          	endbr64 
    311f:	55                   	push   rbp
    3120:	48 89 e5             	mov    rbp,rsp
    3123:	89 f8                	mov    eax,edi
    3125:	88 45 fc             	mov    BYTE PTR [rbp-0x4],al
    3128:	0f be 45 fc          	movsx  eax,BYTE PTR [rbp-0x4]
    312c:	c1 e0 04             	shl    eax,0x4
    312f:	0f b6 d0             	movzx  edx,al
    3132:	0f b6 45 fc          	movzx  eax,BYTE PTR [rbp-0x4]
    3136:	c0 f8 04             	sar    al,0x4
    3139:	0f be c0             	movsx  eax,al
    313c:	01 d0                	add    eax,edx
    313e:	3d f5 00 00 00       	cmp    eax,0xf5
    3143:	0f 94 c0             	sete   al
    3146:	5d                   	pop    rbp
    3147:	c3                   	ret    

0000000000003148 <f408757>:
    3148:	f3 0f 1e fa          	endbr64 
    314c:	55                   	push   rbp
    314d:	48 89 e5             	mov    rbp,rsp
    3150:	89 f8                	mov    eax,edi
    3152:	88 45 fc             	mov    BYTE PTR [rbp-0x4],al
    3155:	0f be 45 fc          	movsx  eax,BYTE PTR [rbp-0x4]
    3159:	c1 e0 04             	shl    eax,0x4
    315c:	0f b6 d0             	movzx  edx,al
    315f:	0f b6 45 fc          	movzx  eax,BYTE PTR [rbp-0x4]
    3163:	c0 f8 04             	sar    al,0x4
    3166:	0f be c0             	movsx  eax,al
    3169:	01 d0                	add    eax,edx
    316b:	83 f8 56             	cmp    eax,0x56
    316e:	0f 94 c0             	sete   al
    3171:	5d                   	pop    rbp
    3172:	c3                   	ret    

0000000000003173 <f7515021>:
    3173:	f3 0f 1e fa          	endbr64 
    3177:	55                   	push   rbp
    3178:	48 89 e5             	mov    rbp,rsp
    317b:	89 f8                	mov    eax,edi
    317d:	88 45 fc             	mov    BYTE PTR [rbp-0x4],al
    3180:	0f be 45 fc          	movsx  eax,BYTE PTR [rbp-0x4]
    3184:	c1 e0 04             	shl    eax,0x4
    3187:	0f b6 d0             	movzx  edx,al
    318a:	0f b6 45 fc          	movzx  eax,BYTE PTR [rbp-0x4]
    318e:	c0 f8 04             	sar    al,0x4
    3191:	0f be c0             	movsx  eax,al
    3194:	01 d0                	add    eax,edx
    3196:	83 f8 43             	cmp    eax,0x43
    3199:	0f 94 c0             	sete   al
    319c:	5d                   	pop    rbp
    319d:	c3                   	ret    

000000000000319e <f5079579>:
    319e:	f3 0f 1e fa          	endbr64 
    31a2:	55                   	push   rbp
    31a3:	48 89 e5             	mov    rbp,rsp
    31a6:	89 f8                	mov    eax,edi
    31a8:	88 45 fc             	mov    BYTE PTR [rbp-0x4],al
    31ab:	0f be 45 fc          	movsx  eax,BYTE PTR [rbp-0x4]
    31af:	c1 e0 04             	shl    eax,0x4
    31b2:	0f b6 d0             	movzx  edx,al
    31b5:	0f b6 45 fc          	movzx  eax,BYTE PTR [rbp-0x4]
    31b9:	c0 f8 04             	sar    al,0x4
    31bc:	0f be c0             	movsx  eax,al
    31bf:	01 d0                	add    eax,edx
    31c1:	83 f8 37             	cmp    eax,0x37
    31c4:	0f 94 c0             	sete   al
    31c7:	5d                   	pop    rbp
    31c8:	c3                   	ret    

00000000000031c9 <f1334508>:
    31c9:	f3 0f 1e fa          	endbr64 
    31cd:	55                   	push   rbp
    31ce:	48 89 e5             	mov    rbp,rsp
    31d1:	89 f8                	mov    eax,edi
    31d3:	88 45 fc             	mov    BYTE PTR [rbp-0x4],al
    31d6:	0f be 45 fc          	movsx  eax,BYTE PTR [rbp-0x4]
    31da:	c1 e0 04             	shl    eax,0x4
    31dd:	0f b6 d0             	movzx  edx,al
    31e0:	0f b6 45 fc          	movzx  eax,BYTE PTR [rbp-0x4]
    31e4:	c0 f8 04             	sar    al,0x4
    31e7:	0f be c0             	movsx  eax,al
    31ea:	01 d0                	add    eax,edx
    31ec:	3d 97 00 00 00       	cmp    eax,0x97
    31f1:	0f 94 c0             	sete   al
    31f4:	5d                   	pop    rbp
    31f5:	c3                   	ret    

00000000000031f6 <f2006371>:
    31f6:	f3 0f 1e fa          	endbr64 
    31fa:	55                   	push   rbp
    31fb:	48 89 e5             	mov    rbp,rsp
    31fe:	89 f8                	mov    eax,edi
    3200:	88 45 fc             	mov    BYTE PTR [rbp-0x4],al
    3203:	0f be 45 fc          	movsx  eax,BYTE PTR [rbp-0x4]
    3207:	c1 e0 04             	shl    eax,0x4
    320a:	0f b6 d0             	movzx  edx,al
    320d:	0f b6 45 fc          	movzx  eax,BYTE PTR [rbp-0x4]
    3211:	c0 f8 04             	sar    al,0x4
    3214:	0f be c0             	movsx  eax,al
    3217:	01 d0                	add    eax,edx
    3219:	3d f5 00 00 00       	cmp    eax,0xf5
    321e:	0f 94 c0             	sete   al
    3221:	5d                   	pop    rbp
    3222:	c3                   	ret    

0000000000003223 <f8066792>:
    3223:	f3 0f 1e fa          	endbr64 
    3227:	55                   	push   rbp
    3228:	48 89 e5             	mov    rbp,rsp
    322b:	89 f8                	mov    eax,edi
    322d:	88 45 fc             	mov    BYTE PTR [rbp-0x4],al
    3230:	0f be 45 fc          	movsx  eax,BYTE PTR [rbp-0x4]
    3234:	c1 e0 04             	shl    eax,0x4
    3237:	0f b6 d0             	movzx  edx,al
    323a:	0f b6 45 fc          	movzx  eax,BYTE PTR [rbp-0x4]
    323e:	c0 f8 04             	sar    al,0x4
    3241:	0f be c0             	movsx  eax,al
    3244:	01 d0                	add    eax,edx
    3246:	83 f8 36             	cmp    eax,0x36
    3249:	0f 94 c0             	sete   al
    324c:	5d                   	pop    rbp
    324d:	c3                   	ret    

000000000000324e <f3842174>:
    324e:	f3 0f 1e fa          	endbr64 
    3252:	55                   	push   rbp
    3253:	48 89 e5             	mov    rbp,rsp
    3256:	89 f8                	mov    eax,edi
    3258:	88 45 fc             	mov    BYTE PTR [rbp-0x4],al
    325b:	0f be 45 fc          	movsx  eax,BYTE PTR [rbp-0x4]
    325f:	c1 e0 04             	shl    eax,0x4
    3262:	0f b6 d0             	movzx  edx,al
    3265:	0f b6 45 fc          	movzx  eax,BYTE PTR [rbp-0x4]
    3269:	c0 f8 04             	sar    al,0x4
    326c:	0f be c0             	movsx  eax,al
    326f:	01 d0                	add    eax,edx
    3271:	3d 86 00 00 00       	cmp    eax,0x86
    3276:	0f 94 c0             	sete   al
    3279:	5d                   	pop    rbp
    327a:	c3                   	ret    

000000000000327b <f1988839>:
    327b:	f3 0f 1e fa          	endbr64 
    327f:	55                   	push   rbp
    3280:	48 89 e5             	mov    rbp,rsp
    3283:	89 f8                	mov    eax,edi
    3285:	88 45 fc             	mov    BYTE PTR [rbp-0x4],al
    3288:	0f be 45 fc          	movsx  eax,BYTE PTR [rbp-0x4]
    328c:	c1 e0 04             	shl    eax,0x4
    328f:	0f b6 d0             	movzx  edx,al
    3292:	0f b6 45 fc          	movzx  eax,BYTE PTR [rbp-0x4]
    3296:	c0 f8 04             	sar    al,0x4
    3299:	0f be c0             	movsx  eax,al
    329c:	01 d0                	add    eax,edx
    329e:	83 f8 43             	cmp    eax,0x43
    32a1:	0f 94 c0             	sete   al
    32a4:	5d                   	pop    rbp
    32a5:	c3                   	ret    

00000000000032a6 <f9928926>:
    32a6:	f3 0f 1e fa          	endbr64 
    32aa:	55                   	push   rbp
    32ab:	48 89 e5             	mov    rbp,rsp
    32ae:	89 f8                	mov    eax,edi
    32b0:	88 45 fc             	mov    BYTE PTR [rbp-0x4],al
    32b3:	0f be 45 fc          	movsx  eax,BYTE PTR [rbp-0x4]
    32b7:	c1 e0 04             	shl    eax,0x4
    32ba:	0f b6 d0             	movzx  edx,al
    32bd:	0f b6 45 fc          	movzx  eax,BYTE PTR [rbp-0x4]
    32c1:	c0 f8 04             	sar    al,0x4
    32c4:	0f be c0             	movsx  eax,al
    32c7:	01 d0                	add    eax,edx
    32c9:	3d c6 00 00 00       	cmp    eax,0xc6
    32ce:	0f 94 c0             	sete   al
    32d1:	5d                   	pop    rbp
    32d2:	c3                   	ret    

00000000000032d3 <f8960275>:
    32d3:	f3 0f 1e fa          	endbr64 
    32d7:	55                   	push   rbp
    32d8:	48 89 e5             	mov    rbp,rsp
    32db:	89 f8                	mov    eax,edi
    32dd:	88 45 fc             	mov    BYTE PTR [rbp-0x4],al
    32e0:	0f be 45 fc          	movsx  eax,BYTE PTR [rbp-0x4]
    32e4:	c1 e0 04             	shl    eax,0x4
    32e7:	0f b6 d0             	movzx  edx,al
    32ea:	0f b6 45 fc          	movzx  eax,BYTE PTR [rbp-0x4]
    32ee:	c0 f8 04             	sar    al,0x4
    32f1:	0f be c0             	movsx  eax,al
    32f4:	01 d0                	add    eax,edx
    32f6:	3d c6 00 00 00       	cmp    eax,0xc6
    32fb:	0f 94 c0             	sete   al
    32fe:	5d                   	pop    rbp
    32ff:	c3                   	ret    

0000000000003300 <f5663288>:
    3300:	f3 0f 1e fa          	endbr64 
    3304:	55                   	push   rbp
    3305:	48 89 e5             	mov    rbp,rsp
    3308:	89 f8                	mov    eax,edi
    330a:	88 45 fc             	mov    BYTE PTR [rbp-0x4],al
    330d:	0f be 45 fc          	movsx  eax,BYTE PTR [rbp-0x4]
    3311:	c1 e0 04             	shl    eax,0x4
    3314:	0f b6 d0             	movzx  edx,al
    3317:	0f b6 45 fc          	movzx  eax,BYTE PTR [rbp-0x4]
    331b:	c0 f8 04             	sar    al,0x4
    331e:	0f be c0             	movsx  eax,al
    3321:	01 d0                	add    eax,edx
    3323:	83 f8 33             	cmp    eax,0x33
    3326:	0f 94 c0             	sete   al
    3329:	5d                   	pop    rbp
    332a:	c3                   	ret    

000000000000332b <f1103067>:
    332b:	f3 0f 1e fa          	endbr64 
    332f:	55                   	push   rbp
    3330:	48 89 e5             	mov    rbp,rsp
    3333:	89 f8                	mov    eax,edi
    3335:	88 45 fc             	mov    BYTE PTR [rbp-0x4],al
    3338:	0f be 45 fc          	movsx  eax,BYTE PTR [rbp-0x4]
    333c:	c1 e0 04             	shl    eax,0x4
    333f:	0f b6 d0             	movzx  edx,al
    3342:	0f b6 45 fc          	movzx  eax,BYTE PTR [rbp-0x4]
    3346:	c0 f8 04             	sar    al,0x4
    3349:	0f be c0             	movsx  eax,al
    334c:	01 d0                	add    eax,edx
    334e:	3d e6 00 00 00       	cmp    eax,0xe6
    3353:	0f 94 c0             	sete   al
    3356:	5d                   	pop    rbp
    3357:	c3                   	ret    

0000000000003358 <f4973817>:
    3358:	f3 0f 1e fa          	endbr64 
    335c:	55                   	push   rbp
    335d:	48 89 e5             	mov    rbp,rsp
    3360:	89 f8                	mov    eax,edi
    3362:	88 45 fc             	mov    BYTE PTR [rbp-0x4],al
    3365:	0f be 45 fc          	movsx  eax,BYTE PTR [rbp-0x4]
    3369:	c1 e0 04             	shl    eax,0x4
    336c:	0f b6 d0             	movzx  edx,al
    336f:	0f b6 45 fc          	movzx  eax,BYTE PTR [rbp-0x4]
    3373:	c0 f8 04             	sar    al,0x4
    3376:	0f be c0             	movsx  eax,al
    3379:	01 d0                	add    eax,edx
    337b:	83 f8 76             	cmp    eax,0x76
    337e:	0f 94 c0             	sete   al
    3381:	5d                   	pop    rbp
    3382:	c3                   	ret    

0000000000003383 <f5477172>:
    3383:	f3 0f 1e fa          	endbr64 
    3387:	55                   	push   rbp
    3388:	48 89 e5             	mov    rbp,rsp
    338b:	89 f8                	mov    eax,edi
    338d:	88 45 fc             	mov    BYTE PTR [rbp-0x4],al
    3390:	0f be 45 fc          	movsx  eax,BYTE PTR [rbp-0x4]
    3394:	c1 e0 04             	shl    eax,0x4
    3397:	0f b6 d0             	movzx  edx,al
    339a:	0f b6 45 fc          	movzx  eax,BYTE PTR [rbp-0x4]
    339e:	c0 f8 04             	sar    al,0x4
    33a1:	0f be c0             	movsx  eax,al
    33a4:	01 d0                	add    eax,edx
    33a6:	83 f8 33             	cmp    eax,0x33
    33a9:	0f 94 c0             	sete   al
    33ac:	5d                   	pop    rbp
    33ad:	c3                   	ret    

00000000000033ae <f4124796>:
    33ae:	f3 0f 1e fa          	endbr64 
    33b2:	55                   	push   rbp
    33b3:	48 89 e5             	mov    rbp,rsp
    33b6:	89 f8                	mov    eax,edi
    33b8:	88 45 fc             	mov    BYTE PTR [rbp-0x4],al
    33bb:	0f be 45 fc          	movsx  eax,BYTE PTR [rbp-0x4]
    33bf:	c1 e0 04             	shl    eax,0x4
    33c2:	0f b6 d0             	movzx  edx,al
    33c5:	0f b6 45 fc          	movzx  eax,BYTE PTR [rbp-0x4]
    33c9:	c0 f8 04             	sar    al,0x4
    33cc:	0f be c0             	movsx  eax,al
    33cf:	01 d0                	add    eax,edx
    33d1:	3d d7 00 00 00       	cmp    eax,0xd7
    33d6:	0f 94 c0             	sete   al
    33d9:	5d                   	pop    rbp
    33da:	c3                   	ret    

00000000000033db <main>:
    33db:	f3 0f 1e fa          	endbr64 
    33df:	55                   	push   rbp
    33e0:	48 89 e5             	mov    rbp,rsp
    33e3:	48 81 ec 10 01 00 00 	sub    rsp,0x110
    33ea:	64 48 8b 04 25 28 00 	mov    rax,QWORD PTR fs:0x28
    33f1:	00 00 
    33f3:	48 89 45 f8          	mov    QWORD PTR [rbp-0x8],rax
    33f7:	31 c0                	xor    eax,eax
    33f9:	48 8d 85 f0 fe ff ff 	lea    rax,[rbp-0x110]
    3400:	ba c8 00 00 00       	mov    edx,0xc8
    3405:	48 89 c6             	mov    rsi,rax
    3408:	bf 00 00 00 00       	mov    edi,0x0
    340d:	e8 7e dc ff ff       	call   1090 <read@plt>
    3412:	0f b6 85 f0 fe ff ff 	movzx  eax,BYTE PTR [rbp-0x110]
    3419:	0f be c0             	movsx  eax,al
    341c:	89 c7                	mov    edi,eax
    341e:	e8 66 dd ff ff       	call   1189 <f122323>
    3423:	84 c0                	test   al,al
    3425:	0f 84 b9 12 00 00    	je     46e4 <main+0x1309>
    342b:	0f b6 85 f1 fe ff ff 	movzx  eax,BYTE PTR [rbp-0x10f]
    3432:	0f be c0             	movsx  eax,al
    3435:	89 c7                	mov    edi,eax
    3437:	e8 78 dd ff ff       	call   11b4 <f7093176>
    343c:	84 c0                	test   al,al
    343e:	0f 84 a0 12 00 00    	je     46e4 <main+0x1309>
    3444:	0f b6 85 f2 fe ff ff 	movzx  eax,BYTE PTR [rbp-0x10e]
    344b:	0f be c0             	movsx  eax,al
    344e:	89 c7                	mov    edi,eax
    3450:	e8 8a dd ff ff       	call   11df <f2267326>
    3455:	84 c0                	test   al,al
    3457:	0f 84 87 12 00 00    	je     46e4 <main+0x1309>
    345d:	0f b6 85 f3 fe ff ff 	movzx  eax,BYTE PTR [rbp-0x10d]
    3464:	0f be c0             	movsx  eax,al
    3467:	89 c7                	mov    edi,eax
    3469:	e8 9c dd ff ff       	call   120a <f3113161>
    346e:	84 c0                	test   al,al
    3470:	0f 84 6e 12 00 00    	je     46e4 <main+0x1309>
    3476:	0f b6 85 f4 fe ff ff 	movzx  eax,BYTE PTR [rbp-0x10c]
    347d:	0f be c0             	movsx  eax,al
    3480:	89 c7                	mov    edi,eax
    3482:	e8 b0 dd ff ff       	call   1237 <f6910364>
    3487:	84 c0                	test   al,al
    3489:	0f 84 55 12 00 00    	je     46e4 <main+0x1309>
    348f:	0f b6 85 f5 fe ff ff 	movzx  eax,BYTE PTR [rbp-0x10b]
    3496:	0f be c0             	movsx  eax,al
    3499:	89 c7                	mov    edi,eax
    349b:	e8 c2 dd ff ff       	call   1262 <f4838080>
    34a0:	84 c0                	test   al,al
    34a2:	0f 84 3c 12 00 00    	je     46e4 <main+0x1309>
    34a8:	0f b6 85 f6 fe ff ff 	movzx  eax,BYTE PTR [rbp-0x10a]
    34af:	0f be c0             	movsx  eax,al
    34b2:	89 c7                	mov    edi,eax
    34b4:	e8 d6 dd ff ff       	call   128f <f3576179>
    34b9:	84 c0                	test   al,al
    34bb:	0f 84 23 12 00 00    	je     46e4 <main+0x1309>
    34c1:	0f b6 85 f7 fe ff ff 	movzx  eax,BYTE PTR [rbp-0x109]
    34c8:	0f be c0             	movsx  eax,al
    34cb:	89 c7                	mov    edi,eax
    34cd:	e8 ea dd ff ff       	call   12bc <f1715128>
    34d2:	84 c0                	test   al,al
    34d4:	0f 84 0a 12 00 00    	je     46e4 <main+0x1309>
    34da:	0f b6 85 f8 fe ff ff 	movzx  eax,BYTE PTR [rbp-0x108]
    34e1:	0f be c0             	movsx  eax,al
    34e4:	89 c7                	mov    edi,eax
    34e6:	e8 fe dd ff ff       	call   12e9 <f4029468>
    34eb:	84 c0                	test   al,al
    34ed:	0f 84 f1 11 00 00    	je     46e4 <main+0x1309>
    34f3:	0f b6 85 f9 fe ff ff 	movzx  eax,BYTE PTR [rbp-0x107]
    34fa:	0f be c0             	movsx  eax,al
    34fd:	89 c7                	mov    edi,eax
    34ff:	e8 10 de ff ff       	call   1314 <f5723857>
    3504:	84 c0                	test   al,al
    3506:	0f 84 d8 11 00 00    	je     46e4 <main+0x1309>
    350c:	0f b6 85 fa fe ff ff 	movzx  eax,BYTE PTR [rbp-0x106]
    3513:	0f be c0             	movsx  eax,al
    3516:	89 c7                	mov    edi,eax
    3518:	e8 22 de ff ff       	call   133f <f5333530>
    351d:	84 c0                	test   al,al
    351f:	0f 84 bf 11 00 00    	je     46e4 <main+0x1309>
    3525:	0f b6 85 fb fe ff ff 	movzx  eax,BYTE PTR [rbp-0x105]
    352c:	0f be c0             	movsx  eax,al
    352f:	89 c7                	mov    edi,eax
    3531:	e8 34 de ff ff       	call   136a <f2200656>
    3536:	84 c0                	test   al,al
    3538:	0f 84 a6 11 00 00    	je     46e4 <main+0x1309>
    353e:	0f b6 85 fc fe ff ff 	movzx  eax,BYTE PTR [rbp-0x104]
    3545:	0f be c0             	movsx  eax,al
    3548:	89 c7                	mov    edi,eax
    354a:	e8 48 de ff ff       	call   1397 <f5832933>
    354f:	84 c0                	test   al,al
    3551:	0f 84 8d 11 00 00    	je     46e4 <main+0x1309>
    3557:	0f b6 85 fd fe ff ff 	movzx  eax,BYTE PTR [rbp-0x103]
    355e:	0f be c0             	movsx  eax,al
    3561:	89 c7                	mov    edi,eax
    3563:	e8 5c de ff ff       	call   13c4 <f162470>
    3568:	84 c0                	test   al,al
    356a:	0f 84 74 11 00 00    	je     46e4 <main+0x1309>
    3570:	0f b6 85 fe fe ff ff 	movzx  eax,BYTE PTR [rbp-0x102]
    3577:	0f be c0             	movsx  eax,al
    357a:	89 c7                	mov    edi,eax
    357c:	e8 6e de ff ff       	call   13ef <f9363706>
    3581:	84 c0                	test   al,al
    3583:	0f 84 5b 11 00 00    	je     46e4 <main+0x1309>
    3589:	0f b6 85 ff fe ff ff 	movzx  eax,BYTE PTR [rbp-0x101]
    3590:	0f be c0             	movsx  eax,al
    3593:	89 c7                	mov    edi,eax
    3595:	e8 80 de ff ff       	call   141a <f8682222>
    359a:	84 c0                	test   al,al
    359c:	0f 84 42 11 00 00    	je     46e4 <main+0x1309>
    35a2:	0f b6 85 00 ff ff ff 	movzx  eax,BYTE PTR [rbp-0x100]
    35a9:	0f be c0             	movsx  eax,al
    35ac:	89 c7                	mov    edi,eax
    35ae:	e8 94 de ff ff       	call   1447 <f5150019>
    35b3:	84 c0                	test   al,al
    35b5:	0f 84 29 11 00 00    	je     46e4 <main+0x1309>
    35bb:	0f b6 85 01 ff ff ff 	movzx  eax,BYTE PTR [rbp-0xff]
    35c2:	0f be c0             	movsx  eax,al
    35c5:	89 c7                	mov    edi,eax
    35c7:	e8 a6 de ff ff       	call   1472 <f846013>
    35cc:	84 c0                	test   al,al
    35ce:	0f 84 10 11 00 00    	je     46e4 <main+0x1309>
    35d4:	0f b6 85 02 ff ff ff 	movzx  eax,BYTE PTR [rbp-0xfe]
    35db:	0f be c0             	movsx  eax,al
    35de:	89 c7                	mov    edi,eax
    35e0:	e8 b8 de ff ff       	call   149d <f1205907>
    35e5:	84 c0                	test   al,al
    35e7:	0f 84 f7 10 00 00    	je     46e4 <main+0x1309>
    35ed:	0f b6 85 03 ff ff ff 	movzx  eax,BYTE PTR [rbp-0xfd]
    35f4:	0f be c0             	movsx  eax,al
    35f7:	89 c7                	mov    edi,eax
    35f9:	e8 ca de ff ff       	call   14c8 <f6037610>
    35fe:	84 c0                	test   al,al
    3600:	0f 84 de 10 00 00    	je     46e4 <main+0x1309>
    3606:	0f b6 85 04 ff ff ff 	movzx  eax,BYTE PTR [rbp-0xfc]
    360d:	0f be c0             	movsx  eax,al
    3610:	89 c7                	mov    edi,eax
    3612:	e8 de de ff ff       	call   14f5 <f9848350>
    3617:	84 c0                	test   al,al
    3619:	0f 84 c5 10 00 00    	je     46e4 <main+0x1309>
    361f:	0f b6 85 05 ff ff ff 	movzx  eax,BYTE PTR [rbp-0xfb]
    3626:	0f be c0             	movsx  eax,al
    3629:	89 c7                	mov    edi,eax
    362b:	e8 f2 de ff ff       	call   1522 <f6824915>
    3630:	84 c0                	test   al,al
    3632:	0f 84 ac 10 00 00    	je     46e4 <main+0x1309>
    3638:	0f b6 85 06 ff ff ff 	movzx  eax,BYTE PTR [rbp-0xfa]
    363f:	0f be c0             	movsx  eax,al
    3642:	89 c7                	mov    edi,eax
    3644:	e8 06 df ff ff       	call   154f <f684565>
    3649:	84 c0                	test   al,al
    364b:	0f 84 93 10 00 00    	je     46e4 <main+0x1309>
    3651:	0f b6 85 07 ff ff ff 	movzx  eax,BYTE PTR [rbp-0xf9]
    3658:	0f be c0             	movsx  eax,al
    365b:	89 c7                	mov    edi,eax
    365d:	e8 1a df ff ff       	call   157c <f92520>
    3662:	84 c0                	test   al,al
    3664:	0f 84 7a 10 00 00    	je     46e4 <main+0x1309>
    366a:	0f b6 85 08 ff ff ff 	movzx  eax,BYTE PTR [rbp-0xf8]
    3671:	0f be c0             	movsx  eax,al
    3674:	89 c7                	mov    edi,eax
    3676:	e8 2c df ff ff       	call   15a7 <f2033367>
    367b:	84 c0                	test   al,al
    367d:	0f 84 61 10 00 00    	je     46e4 <main+0x1309>
    3683:	0f b6 85 09 ff ff ff 	movzx  eax,BYTE PTR [rbp-0xf7]
    368a:	0f be c0             	movsx  eax,al
    368d:	89 c7                	mov    edi,eax
    368f:	e8 40 df ff ff       	call   15d4 <f554708>
    3694:	84 c0                	test   al,al
    3696:	0f 84 48 10 00 00    	je     46e4 <main+0x1309>
    369c:	0f b6 85 0a ff ff ff 	movzx  eax,BYTE PTR [rbp-0xf6]
    36a3:	0f be c0             	movsx  eax,al
    36a6:	89 c7                	mov    edi,eax
    36a8:	e8 52 df ff ff       	call   15ff <f5673323>
    36ad:	84 c0                	test   al,al
    36af:	0f 84 2f 10 00 00    	je     46e4 <main+0x1309>
    36b5:	0f b6 85 0b ff ff ff 	movzx  eax,BYTE PTR [rbp-0xf5]
    36bc:	0f be c0             	movsx  eax,al
    36bf:	89 c7                	mov    edi,eax
    36c1:	e8 66 df ff ff       	call   162c <f4231114>
    36c6:	84 c0                	test   al,al
    36c8:	0f 84 16 10 00 00    	je     46e4 <main+0x1309>
    36ce:	0f b6 85 0c ff ff ff 	movzx  eax,BYTE PTR [rbp-0xf4]
    36d5:	0f be c0             	movsx  eax,al
    36d8:	89 c7                	mov    edi,eax
    36da:	e8 7a df ff ff       	call   1659 <f7418636>
    36df:	84 c0                	test   al,al
    36e1:	0f 84 fd 0f 00 00    	je     46e4 <main+0x1309>
    36e7:	0f b6 85 0d ff ff ff 	movzx  eax,BYTE PTR [rbp-0xf3]
    36ee:	0f be c0             	movsx  eax,al
    36f1:	89 c7                	mov    edi,eax
    36f3:	e8 8c df ff ff       	call   1684 <f1853358>
    36f8:	84 c0                	test   al,al
    36fa:	0f 84 e4 0f 00 00    	je     46e4 <main+0x1309>
    3700:	0f b6 85 0e ff ff ff 	movzx  eax,BYTE PTR [rbp-0xf2]
    3707:	0f be c0             	movsx  eax,al
    370a:	89 c7                	mov    edi,eax
    370c:	e8 a0 df ff ff       	call   16b1 <f1991208>
    3711:	84 c0                	test   al,al
    3713:	0f 84 cb 0f 00 00    	je     46e4 <main+0x1309>
    3719:	0f b6 85 0f ff ff ff 	movzx  eax,BYTE PTR [rbp-0xf1]
    3720:	0f be c0             	movsx  eax,al
    3723:	89 c7                	mov    edi,eax
    3725:	e8 b4 df ff ff       	call   16de <f6976528>
    372a:	84 c0                	test   al,al
    372c:	0f 84 b2 0f 00 00    	je     46e4 <main+0x1309>
    3732:	0f b6 85 10 ff ff ff 	movzx  eax,BYTE PTR [rbp-0xf0]
    3739:	0f be c0             	movsx  eax,al
    373c:	89 c7                	mov    edi,eax
    373e:	e8 c8 df ff ff       	call   170b <f3698419>
    3743:	84 c0                	test   al,al
    3745:	0f 84 99 0f 00 00    	je     46e4 <main+0x1309>
    374b:	0f b6 85 11 ff ff ff 	movzx  eax,BYTE PTR [rbp-0xef]
    3752:	0f be c0             	movsx  eax,al
    3755:	89 c7                	mov    edi,eax
    3757:	e8 da df ff ff       	call   1736 <f2566491>
    375c:	84 c0                	test   al,al
    375e:	0f 84 80 0f 00 00    	je     46e4 <main+0x1309>
    3764:	0f b6 85 12 ff ff ff 	movzx  eax,BYTE PTR [rbp-0xee]
    376b:	0f be c0             	movsx  eax,al
    376e:	89 c7                	mov    edi,eax
    3770:	e8 ee df ff ff       	call   1763 <f7994952>
    3775:	84 c0                	test   al,al
    3777:	0f 84 67 0f 00 00    	je     46e4 <main+0x1309>
    377d:	0f b6 85 13 ff ff ff 	movzx  eax,BYTE PTR [rbp-0xed]
    3784:	0f be c0             	movsx  eax,al
    3787:	89 c7                	mov    edi,eax
    3789:	e8 00 e0 ff ff       	call   178e <f5140713>
    378e:	84 c0                	test   al,al
    3790:	0f 84 4e 0f 00 00    	je     46e4 <main+0x1309>
    3796:	0f b6 85 14 ff ff ff 	movzx  eax,BYTE PTR [rbp-0xec]
    379d:	0f be c0             	movsx  eax,al
    37a0:	89 c7                	mov    edi,eax
    37a2:	e8 12 e0 ff ff       	call   17b9 <f88780>
    37a7:	84 c0                	test   al,al
    37a9:	0f 84 35 0f 00 00    	je     46e4 <main+0x1309>
    37af:	0f b6 85 15 ff ff ff 	movzx  eax,BYTE PTR [rbp-0xeb]
    37b6:	0f be c0             	movsx  eax,al
    37b9:	89 c7                	mov    edi,eax
    37bb:	e8 26 e0 ff ff       	call   17e6 <f2161814>
    37c0:	84 c0                	test   al,al
    37c2:	0f 84 1c 0f 00 00    	je     46e4 <main+0x1309>
    37c8:	0f b6 85 16 ff ff ff 	movzx  eax,BYTE PTR [rbp-0xea]
    37cf:	0f be c0             	movsx  eax,al
    37d2:	89 c7                	mov    edi,eax
    37d4:	e8 3a e0 ff ff       	call   1813 <f9633522>
    37d9:	84 c0                	test   al,al
    37db:	0f 84 03 0f 00 00    	je     46e4 <main+0x1309>
    37e1:	0f b6 85 17 ff ff ff 	movzx  eax,BYTE PTR [rbp-0xe9]
    37e8:	0f be c0             	movsx  eax,al
    37eb:	89 c7                	mov    edi,eax
    37ed:	e8 4c e0 ff ff       	call   183e <f4283702>
    37f2:	84 c0                	test   al,al
    37f4:	0f 84 ea 0e 00 00    	je     46e4 <main+0x1309>
    37fa:	0f b6 85 18 ff ff ff 	movzx  eax,BYTE PTR [rbp-0xe8]
    3801:	0f be c0             	movsx  eax,al
    3804:	89 c7                	mov    edi,eax
    3806:	e8 5e e0 ff ff       	call   1869 <f4865077>
    380b:	84 c0                	test   al,al
    380d:	0f 84 d1 0e 00 00    	je     46e4 <main+0x1309>
    3813:	0f b6 85 19 ff ff ff 	movzx  eax,BYTE PTR [rbp-0xe7]
    381a:	0f be c0             	movsx  eax,al
    381d:	89 c7                	mov    edi,eax
    381f:	e8 72 e0 ff ff       	call   1896 <f5077469>
    3824:	84 c0                	test   al,al
    3826:	0f 84 b8 0e 00 00    	je     46e4 <main+0x1309>
    382c:	0f b6 85 1a ff ff ff 	movzx  eax,BYTE PTR [rbp-0xe6]
    3833:	0f be c0             	movsx  eax,al
    3836:	89 c7                	mov    edi,eax
    3838:	e8 84 e0 ff ff       	call   18c1 <f8942470>
    383d:	84 c0                	test   al,al
    383f:	0f 84 9f 0e 00 00    	je     46e4 <main+0x1309>
    3845:	0f b6 85 1b ff ff ff 	movzx  eax,BYTE PTR [rbp-0xe5]
    384c:	0f be c0             	movsx  eax,al
    384f:	89 c7                	mov    edi,eax
    3851:	e8 96 e0 ff ff       	call   18ec <f69599>
    3856:	84 c0                	test   al,al
    3858:	0f 84 86 0e 00 00    	je     46e4 <main+0x1309>
    385e:	0f b6 85 1c ff ff ff 	movzx  eax,BYTE PTR [rbp-0xe4]
    3865:	0f be c0             	movsx  eax,al
    3868:	89 c7                	mov    edi,eax
    386a:	e8 aa e0 ff ff       	call   1919 <f306115>
    386f:	84 c0                	test   al,al
    3871:	0f 84 6d 0e 00 00    	je     46e4 <main+0x1309>
    3877:	0f b6 85 1d ff ff ff 	movzx  eax,BYTE PTR [rbp-0xe3]
    387e:	0f be c0             	movsx  eax,al
    3881:	89 c7                	mov    edi,eax
    3883:	e8 be e0 ff ff       	call   1946 <f5819085>
    3888:	84 c0                	test   al,al
    388a:	0f 84 54 0e 00 00    	je     46e4 <main+0x1309>
    3890:	0f b6 85 1e ff ff ff 	movzx  eax,BYTE PTR [rbp-0xe2]
    3897:	0f be c0             	movsx  eax,al
    389a:	89 c7                	mov    edi,eax
    389c:	e8 d0 e0 ff ff       	call   1971 <f2051229>
    38a1:	84 c0                	test   al,al
    38a3:	0f 84 3b 0e 00 00    	je     46e4 <main+0x1309>
    38a9:	0f b6 85 1f ff ff ff 	movzx  eax,BYTE PTR [rbp-0xe1]
    38b0:	0f be c0             	movsx  eax,al
    38b3:	89 c7                	mov    edi,eax
    38b5:	e8 e2 e0 ff ff       	call   199c <f8121604>
    38ba:	84 c0                	test   al,al
    38bc:	0f 84 22 0e 00 00    	je     46e4 <main+0x1309>
    38c2:	0f b6 85 20 ff ff ff 	movzx  eax,BYTE PTR [rbp-0xe0]
    38c9:	0f be c0             	movsx  eax,al
    38cc:	89 c7                	mov    edi,eax
    38ce:	e8 f6 e0 ff ff       	call   19c9 <f5595266>
    38d3:	84 c0                	test   al,al
    38d5:	0f 84 09 0e 00 00    	je     46e4 <main+0x1309>
    38db:	0f b6 85 21 ff ff ff 	movzx  eax,BYTE PTR [rbp-0xdf]
    38e2:	0f be c0             	movsx  eax,al
    38e5:	89 c7                	mov    edi,eax
    38e7:	e8 0a e1 ff ff       	call   19f6 <f3404320>
    38ec:	84 c0                	test   al,al
    38ee:	0f 84 f0 0d 00 00    	je     46e4 <main+0x1309>
    38f4:	0f b6 85 22 ff ff ff 	movzx  eax,BYTE PTR [rbp-0xde]
    38fb:	0f be c0             	movsx  eax,al
    38fe:	89 c7                	mov    edi,eax
    3900:	e8 1c e1 ff ff       	call   1a21 <f4356041>
    3905:	84 c0                	test   al,al
    3907:	0f 84 d7 0d 00 00    	je     46e4 <main+0x1309>
    390d:	0f b6 85 23 ff ff ff 	movzx  eax,BYTE PTR [rbp-0xdd]
    3914:	0f be c0             	movsx  eax,al
    3917:	89 c7                	mov    edi,eax
    3919:	e8 30 e1 ff ff       	call   1a4e <f3676482>
    391e:	84 c0                	test   al,al
    3920:	0f 84 be 0d 00 00    	je     46e4 <main+0x1309>
    3926:	0f b6 85 24 ff ff ff 	movzx  eax,BYTE PTR [rbp-0xdc]
    392d:	0f be c0             	movsx  eax,al
    3930:	89 c7                	mov    edi,eax
    3932:	e8 42 e1 ff ff       	call   1a79 <f285854>
    3937:	84 c0                	test   al,al
    3939:	0f 84 a5 0d 00 00    	je     46e4 <main+0x1309>
    393f:	0f b6 85 25 ff ff ff 	movzx  eax,BYTE PTR [rbp-0xdb]
    3946:	0f be c0             	movsx  eax,al
    3949:	89 c7                	mov    edi,eax
    394b:	e8 54 e1 ff ff       	call   1aa4 <f4534378>
    3950:	84 c0                	test   al,al
    3952:	0f 84 8c 0d 00 00    	je     46e4 <main+0x1309>
    3958:	0f b6 85 26 ff ff ff 	movzx  eax,BYTE PTR [rbp-0xda]
    395f:	0f be c0             	movsx  eax,al
    3962:	89 c7                	mov    edi,eax
    3964:	e8 68 e1 ff ff       	call   1ad1 <f5431748>
    3969:	84 c0                	test   al,al
    396b:	0f 84 73 0d 00 00    	je     46e4 <main+0x1309>
    3971:	0f b6 85 27 ff ff ff 	movzx  eax,BYTE PTR [rbp-0xd9]
    3978:	0f be c0             	movsx  eax,al
    397b:	89 c7                	mov    edi,eax
    397d:	e8 7c e1 ff ff       	call   1afe <f3034080>
    3982:	84 c0                	test   al,al
    3984:	0f 84 5a 0d 00 00    	je     46e4 <main+0x1309>
    398a:	0f b6 85 28 ff ff ff 	movzx  eax,BYTE PTR [rbp-0xd8]
    3991:	0f be c0             	movsx  eax,al
    3994:	89 c7                	mov    edi,eax
    3996:	e8 8e e1 ff ff       	call   1b29 <f6793597>
    399b:	84 c0                	test   al,al
    399d:	0f 84 41 0d 00 00    	je     46e4 <main+0x1309>
    39a3:	0f b6 85 29 ff ff ff 	movzx  eax,BYTE PTR [rbp-0xd7]
    39aa:	0f be c0             	movsx  eax,al
    39ad:	89 c7                	mov    edi,eax
    39af:	e8 a2 e1 ff ff       	call   1b56 <f2069805>
    39b4:	84 c0                	test   al,al
    39b6:	0f 84 28 0d 00 00    	je     46e4 <main+0x1309>
    39bc:	0f b6 85 2a ff ff ff 	movzx  eax,BYTE PTR [rbp-0xd6]
    39c3:	0f be c0             	movsx  eax,al
    39c6:	89 c7                	mov    edi,eax
    39c8:	e8 b4 e1 ff ff       	call   1b81 <f4427480>
    39cd:	84 c0                	test   al,al
    39cf:	0f 84 0f 0d 00 00    	je     46e4 <main+0x1309>
    39d5:	0f b6 85 2b ff ff ff 	movzx  eax,BYTE PTR [rbp-0xd5]
    39dc:	0f be c0             	movsx  eax,al
    39df:	89 c7                	mov    edi,eax
    39e1:	e8 c6 e1 ff ff       	call   1bac <f6745606>
    39e6:	84 c0                	test   al,al
    39e8:	0f 84 f6 0c 00 00    	je     46e4 <main+0x1309>
    39ee:	0f b6 85 2c ff ff ff 	movzx  eax,BYTE PTR [rbp-0xd4]
    39f5:	0f be c0             	movsx  eax,al
    39f8:	89 c7                	mov    edi,eax
    39fa:	e8 da e1 ff ff       	call   1bd9 <f8019149>
    39ff:	84 c0                	test   al,al
    3a01:	0f 84 dd 0c 00 00    	je     46e4 <main+0x1309>
    3a07:	0f b6 85 2d ff ff ff 	movzx  eax,BYTE PTR [rbp-0xd3]
    3a0e:	0f be c0             	movsx  eax,al
    3a11:	89 c7                	mov    edi,eax
    3a13:	e8 ee e1 ff ff       	call   1c06 <f5221954>
    3a18:	84 c0                	test   al,al
    3a1a:	0f 84 c4 0c 00 00    	je     46e4 <main+0x1309>
    3a20:	0f b6 85 2e ff ff ff 	movzx  eax,BYTE PTR [rbp-0xd2]
    3a27:	0f be c0             	movsx  eax,al
    3a2a:	89 c7                	mov    edi,eax
    3a2c:	e8 02 e2 ff ff       	call   1c33 <f6822097>
    3a31:	84 c0                	test   al,al
    3a33:	0f 84 ab 0c 00 00    	je     46e4 <main+0x1309>
    3a39:	0f b6 85 2f ff ff ff 	movzx  eax,BYTE PTR [rbp-0xd1]
    3a40:	0f be c0             	movsx  eax,al
    3a43:	89 c7                	mov    edi,eax
    3a45:	e8 16 e2 ff ff       	call   1c60 <f9144894>
    3a4a:	84 c0                	test   al,al
    3a4c:	0f 84 92 0c 00 00    	je     46e4 <main+0x1309>
    3a52:	0f b6 85 30 ff ff ff 	movzx  eax,BYTE PTR [rbp-0xd0]
    3a59:	0f be c0             	movsx  eax,al
    3a5c:	89 c7                	mov    edi,eax
    3a5e:	e8 2a e2 ff ff       	call   1c8d <f9662054>
    3a63:	84 c0                	test   al,al
    3a65:	0f 84 79 0c 00 00    	je     46e4 <main+0x1309>
    3a6b:	0f b6 85 31 ff ff ff 	movzx  eax,BYTE PTR [rbp-0xcf]
    3a72:	0f be c0             	movsx  eax,al
    3a75:	89 c7                	mov    edi,eax
    3a77:	e8 3e e2 ff ff       	call   1cba <f3474527>
    3a7c:	84 c0                	test   al,al
    3a7e:	0f 84 60 0c 00 00    	je     46e4 <main+0x1309>
    3a84:	0f b6 85 32 ff ff ff 	movzx  eax,BYTE PTR [rbp-0xce]
    3a8b:	0f be c0             	movsx  eax,al
    3a8e:	89 c7                	mov    edi,eax
    3a90:	e8 52 e2 ff ff       	call   1ce7 <f543247>
    3a95:	84 c0                	test   al,al
    3a97:	0f 84 47 0c 00 00    	je     46e4 <main+0x1309>
    3a9d:	0f b6 85 33 ff ff ff 	movzx  eax,BYTE PTR [rbp-0xcd]
    3aa4:	0f be c0             	movsx  eax,al
    3aa7:	89 c7                	mov    edi,eax
    3aa9:	e8 66 e2 ff ff       	call   1d14 <f7109986>
    3aae:	84 c0                	test   al,al
    3ab0:	0f 84 2e 0c 00 00    	je     46e4 <main+0x1309>
    3ab6:	0f b6 85 34 ff ff ff 	movzx  eax,BYTE PTR [rbp-0xcc]
    3abd:	0f be c0             	movsx  eax,al
    3ac0:	89 c7                	mov    edi,eax
    3ac2:	e8 7a e2 ff ff       	call   1d41 <f6472803>
    3ac7:	84 c0                	test   al,al
    3ac9:	0f 84 15 0c 00 00    	je     46e4 <main+0x1309>
    3acf:	0f b6 85 35 ff ff ff 	movzx  eax,BYTE PTR [rbp-0xcb]
    3ad6:	0f be c0             	movsx  eax,al
    3ad9:	89 c7                	mov    edi,eax
    3adb:	e8 8e e2 ff ff       	call   1d6e <f7656586>
    3ae0:	84 c0                	test   al,al
    3ae2:	0f 84 fc 0b 00 00    	je     46e4 <main+0x1309>
    3ae8:	0f b6 85 36 ff ff ff 	movzx  eax,BYTE PTR [rbp-0xca]
    3aef:	0f be c0             	movsx  eax,al
    3af2:	89 c7                	mov    edi,eax
    3af4:	e8 a2 e2 ff ff       	call   1d9b <f2884700>
    3af9:	84 c0                	test   al,al
    3afb:	0f 84 e3 0b 00 00    	je     46e4 <main+0x1309>
    3b01:	0f b6 85 37 ff ff ff 	movzx  eax,BYTE PTR [rbp-0xc9]
    3b08:	0f be c0             	movsx  eax,al
    3b0b:	89 c7                	mov    edi,eax
    3b0d:	e8 b6 e2 ff ff       	call   1dc8 <f8976878>
    3b12:	84 c0                	test   al,al
    3b14:	0f 84 ca 0b 00 00    	je     46e4 <main+0x1309>
    3b1a:	0f b6 85 38 ff ff ff 	movzx  eax,BYTE PTR [rbp-0xc8]
    3b21:	0f be c0             	movsx  eax,al
    3b24:	89 c7                	mov    edi,eax
    3b26:	e8 c8 e2 ff ff       	call   1df3 <f8152608>
    3b2b:	84 c0                	test   al,al
    3b2d:	0f 84 b1 0b 00 00    	je     46e4 <main+0x1309>
    3b33:	0f b6 85 39 ff ff ff 	movzx  eax,BYTE PTR [rbp-0xc7]
    3b3a:	0f be c0             	movsx  eax,al
    3b3d:	89 c7                	mov    edi,eax
    3b3f:	e8 dc e2 ff ff       	call   1e20 <f9818014>
    3b44:	84 c0                	test   al,al
    3b46:	0f 84 98 0b 00 00    	je     46e4 <main+0x1309>
    3b4c:	0f b6 85 3a ff ff ff 	movzx  eax,BYTE PTR [rbp-0xc6]
    3b53:	0f be c0             	movsx  eax,al
    3b56:	89 c7                	mov    edi,eax
    3b58:	e8 ee e2 ff ff       	call   1e4b <f8511877>
    3b5d:	84 c0                	test   al,al
    3b5f:	0f 84 7f 0b 00 00    	je     46e4 <main+0x1309>
    3b65:	0f b6 85 3b ff ff ff 	movzx  eax,BYTE PTR [rbp-0xc5]
    3b6c:	0f be c0             	movsx  eax,al
    3b6f:	89 c7                	mov    edi,eax
    3b71:	e8 02 e3 ff ff       	call   1e78 <f8107564>
    3b76:	84 c0                	test   al,al
    3b78:	0f 84 66 0b 00 00    	je     46e4 <main+0x1309>
    3b7e:	0f b6 85 3c ff ff ff 	movzx  eax,BYTE PTR [rbp-0xc4]
    3b85:	0f be c0             	movsx  eax,al
    3b88:	89 c7                	mov    edi,eax
    3b8a:	e8 16 e3 ff ff       	call   1ea5 <f6805295>
    3b8f:	84 c0                	test   al,al
    3b91:	0f 84 4d 0b 00 00    	je     46e4 <main+0x1309>
    3b97:	0f b6 85 3d ff ff ff 	movzx  eax,BYTE PTR [rbp-0xc3]
    3b9e:	0f be c0             	movsx  eax,al
    3ba1:	89 c7                	mov    edi,eax
    3ba3:	e8 2a e3 ff ff       	call   1ed2 <f7429348>
    3ba8:	84 c0                	test   al,al
    3baa:	0f 84 34 0b 00 00    	je     46e4 <main+0x1309>
    3bb0:	0f b6 85 3e ff ff ff 	movzx  eax,BYTE PTR [rbp-0xc2]
    3bb7:	0f be c0             	movsx  eax,al
    3bba:	89 c7                	mov    edi,eax
    3bbc:	e8 3e e3 ff ff       	call   1eff <f8265912>
    3bc1:	84 c0                	test   al,al
    3bc3:	0f 84 1b 0b 00 00    	je     46e4 <main+0x1309>
    3bc9:	0f b6 85 3f ff ff ff 	movzx  eax,BYTE PTR [rbp-0xc1]
    3bd0:	0f be c0             	movsx  eax,al
    3bd3:	89 c7                	mov    edi,eax
    3bd5:	e8 50 e3 ff ff       	call   1f2a <f3580401>
    3bda:	84 c0                	test   al,al
    3bdc:	0f 84 02 0b 00 00    	je     46e4 <main+0x1309>
    3be2:	0f b6 85 40 ff ff ff 	movzx  eax,BYTE PTR [rbp-0xc0]
    3be9:	0f be c0             	movsx  eax,al
    3bec:	89 c7                	mov    edi,eax
    3bee:	e8 62 e3 ff ff       	call   1f55 <f8346581>
    3bf3:	84 c0                	test   al,al
    3bf5:	0f 84 e9 0a 00 00    	je     46e4 <main+0x1309>
    3bfb:	0f b6 85 41 ff ff ff 	movzx  eax,BYTE PTR [rbp-0xbf]
    3c02:	0f be c0             	movsx  eax,al
    3c05:	89 c7                	mov    edi,eax
    3c07:	e8 76 e3 ff ff       	call   1f82 <f5751977>
    3c0c:	84 c0                	test   al,al
    3c0e:	0f 84 d0 0a 00 00    	je     46e4 <main+0x1309>
    3c14:	0f b6 85 42 ff ff ff 	movzx  eax,BYTE PTR [rbp-0xbe]
    3c1b:	0f be c0             	movsx  eax,al
    3c1e:	89 c7                	mov    edi,eax
    3c20:	e8 88 e3 ff ff       	call   1fad <f3210599>
    3c25:	84 c0                	test   al,al
    3c27:	0f 84 b7 0a 00 00    	je     46e4 <main+0x1309>
    3c2d:	0f b6 85 43 ff ff ff 	movzx  eax,BYTE PTR [rbp-0xbd]
    3c34:	0f be c0             	movsx  eax,al
    3c37:	89 c7                	mov    edi,eax
    3c39:	e8 9a e3 ff ff       	call   1fd8 <f1415318>
    3c3e:	84 c0                	test   al,al
    3c40:	0f 84 9e 0a 00 00    	je     46e4 <main+0x1309>
    3c46:	0f b6 85 44 ff ff ff 	movzx  eax,BYTE PTR [rbp-0xbc]
    3c4d:	0f be c0             	movsx  eax,al
    3c50:	89 c7                	mov    edi,eax
    3c52:	e8 ac e3 ff ff       	call   2003 <f3734500>
    3c57:	84 c0                	test   al,al
    3c59:	0f 84 85 0a 00 00    	je     46e4 <main+0x1309>
    3c5f:	0f b6 85 45 ff ff ff 	movzx  eax,BYTE PTR [rbp-0xbb]
    3c66:	0f be c0             	movsx  eax,al
    3c69:	89 c7                	mov    edi,eax
    3c6b:	e8 be e3 ff ff       	call   202e <f8917722>
    3c70:	84 c0                	test   al,al
    3c72:	0f 84 6c 0a 00 00    	je     46e4 <main+0x1309>
    3c78:	0f b6 85 46 ff ff ff 	movzx  eax,BYTE PTR [rbp-0xba]
    3c7f:	0f be c0             	movsx  eax,al
    3c82:	89 c7                	mov    edi,eax
    3c84:	e8 d0 e3 ff ff       	call   2059 <f7283249>
    3c89:	84 c0                	test   al,al
    3c8b:	0f 84 53 0a 00 00    	je     46e4 <main+0x1309>
    3c91:	0f b6 85 47 ff ff ff 	movzx  eax,BYTE PTR [rbp-0xb9]
    3c98:	0f be c0             	movsx  eax,al
    3c9b:	89 c7                	mov    edi,eax
    3c9d:	e8 e2 e3 ff ff       	call   2084 <f8622882>
    3ca2:	84 c0                	test   al,al
    3ca4:	0f 84 3a 0a 00 00    	je     46e4 <main+0x1309>
    3caa:	0f b6 85 48 ff ff ff 	movzx  eax,BYTE PTR [rbp-0xb8]
    3cb1:	0f be c0             	movsx  eax,al
    3cb4:	89 c7                	mov    edi,eax
    3cb6:	e8 f6 e3 ff ff       	call   20b1 <f1221298>
    3cbb:	84 c0                	test   al,al
    3cbd:	0f 84 21 0a 00 00    	je     46e4 <main+0x1309>
    3cc3:	0f b6 85 49 ff ff ff 	movzx  eax,BYTE PTR [rbp-0xb7]
    3cca:	0f be c0             	movsx  eax,al
    3ccd:	89 c7                	mov    edi,eax
    3ccf:	e8 08 e4 ff ff       	call   20dc <f2575656>
    3cd4:	84 c0                	test   al,al
    3cd6:	0f 84 08 0a 00 00    	je     46e4 <main+0x1309>
    3cdc:	0f b6 85 4a ff ff ff 	movzx  eax,BYTE PTR [rbp-0xb6]
    3ce3:	0f be c0             	movsx  eax,al
    3ce6:	89 c7                	mov    edi,eax
    3ce8:	e8 1a e4 ff ff       	call   2107 <f2048837>
    3ced:	84 c0                	test   al,al
    3cef:	0f 84 ef 09 00 00    	je     46e4 <main+0x1309>
    3cf5:	0f b6 85 4b ff ff ff 	movzx  eax,BYTE PTR [rbp-0xb5]
    3cfc:	0f be c0             	movsx  eax,al
    3cff:	89 c7                	mov    edi,eax
    3d01:	e8 2c e4 ff ff       	call   2132 <f2256059>
    3d06:	84 c0                	test   al,al
    3d08:	0f 84 d6 09 00 00    	je     46e4 <main+0x1309>
    3d0e:	0f b6 85 4c ff ff ff 	movzx  eax,BYTE PTR [rbp-0xb4]
    3d15:	0f be c0             	movsx  eax,al
    3d18:	89 c7                	mov    edi,eax
    3d1a:	e8 40 e4 ff ff       	call   215f <f1257459>
    3d1f:	84 c0                	test   al,al
    3d21:	0f 84 bd 09 00 00    	je     46e4 <main+0x1309>
    3d27:	0f b6 85 4d ff ff ff 	movzx  eax,BYTE PTR [rbp-0xb3]
    3d2e:	0f be c0             	movsx  eax,al
    3d31:	89 c7                	mov    edi,eax
    3d33:	e8 52 e4 ff ff       	call   218a <f5021108>
    3d38:	84 c0                	test   al,al
    3d3a:	0f 84 a4 09 00 00    	je     46e4 <main+0x1309>
    3d40:	0f b6 85 4e ff ff ff 	movzx  eax,BYTE PTR [rbp-0xb2]
    3d47:	0f be c0             	movsx  eax,al
    3d4a:	89 c7                	mov    edi,eax
    3d4c:	e8 64 e4 ff ff       	call   21b5 <f8183340>
    3d51:	84 c0                	test   al,al
    3d53:	0f 84 8b 09 00 00    	je     46e4 <main+0x1309>
    3d59:	0f b6 85 4f ff ff ff 	movzx  eax,BYTE PTR [rbp-0xb1]
    3d60:	0f be c0             	movsx  eax,al
    3d63:	89 c7                	mov    edi,eax
    3d65:	e8 78 e4 ff ff       	call   21e2 <f4188611>
    3d6a:	84 c0                	test   al,al
    3d6c:	0f 84 72 09 00 00    	je     46e4 <main+0x1309>
    3d72:	0f b6 85 50 ff ff ff 	movzx  eax,BYTE PTR [rbp-0xb0]
    3d79:	0f be c0             	movsx  eax,al
    3d7c:	89 c7                	mov    edi,eax
    3d7e:	e8 8a e4 ff ff       	call   220d <f7842102>
    3d83:	84 c0                	test   al,al
    3d85:	0f 84 59 09 00 00    	je     46e4 <main+0x1309>
    3d8b:	0f b6 85 51 ff ff ff 	movzx  eax,BYTE PTR [rbp-0xaf]
    3d92:	0f be c0             	movsx  eax,al
    3d95:	89 c7                	mov    edi,eax
    3d97:	e8 9e e4 ff ff       	call   223a <f5218775>
    3d9c:	84 c0                	test   al,al
    3d9e:	0f 84 40 09 00 00    	je     46e4 <main+0x1309>
    3da4:	0f b6 85 52 ff ff ff 	movzx  eax,BYTE PTR [rbp-0xae]
    3dab:	0f be c0             	movsx  eax,al
    3dae:	89 c7                	mov    edi,eax
    3db0:	e8 b0 e4 ff ff       	call   2265 <f8862806>
    3db5:	84 c0                	test   al,al
    3db7:	0f 84 27 09 00 00    	je     46e4 <main+0x1309>
    3dbd:	0f b6 85 53 ff ff ff 	movzx  eax,BYTE PTR [rbp-0xad]
    3dc4:	0f be c0             	movsx  eax,al
    3dc7:	89 c7                	mov    edi,eax
    3dc9:	e8 c2 e4 ff ff       	call   2290 <f7824321>
    3dce:	84 c0                	test   al,al
    3dd0:	0f 84 0e 09 00 00    	je     46e4 <main+0x1309>
    3dd6:	0f b6 85 54 ff ff ff 	movzx  eax,BYTE PTR [rbp-0xac]
    3ddd:	0f be c0             	movsx  eax,al
    3de0:	89 c7                	mov    edi,eax
    3de2:	e8 d4 e4 ff ff       	call   22bb <f3450917>
    3de7:	84 c0                	test   al,al
    3de9:	0f 84 f5 08 00 00    	je     46e4 <main+0x1309>
    3def:	0f b6 85 55 ff ff ff 	movzx  eax,BYTE PTR [rbp-0xab]
    3df6:	0f be c0             	movsx  eax,al
    3df9:	89 c7                	mov    edi,eax
    3dfb:	e8 e6 e4 ff ff       	call   22e6 <f1224443>
    3e00:	84 c0                	test   al,al
    3e02:	0f 84 dc 08 00 00    	je     46e4 <main+0x1309>
    3e08:	0f b6 85 56 ff ff ff 	movzx  eax,BYTE PTR [rbp-0xaa]
    3e0f:	0f be c0             	movsx  eax,al
    3e12:	89 c7                	mov    edi,eax
    3e14:	e8 fa e4 ff ff       	call   2313 <f1210252>
    3e19:	84 c0                	test   al,al
    3e1b:	0f 84 c3 08 00 00    	je     46e4 <main+0x1309>
    3e21:	0f b6 85 57 ff ff ff 	movzx  eax,BYTE PTR [rbp-0xa9]
    3e28:	0f be c0             	movsx  eax,al
    3e2b:	89 c7                	mov    edi,eax
    3e2d:	e8 0c e5 ff ff       	call   233e <f1011265>
    3e32:	84 c0                	test   al,al
    3e34:	0f 84 aa 08 00 00    	je     46e4 <main+0x1309>
    3e3a:	0f b6 85 58 ff ff ff 	movzx  eax,BYTE PTR [rbp-0xa8]
    3e41:	0f be c0             	movsx  eax,al
    3e44:	89 c7                	mov    edi,eax
    3e46:	e8 1e e5 ff ff       	call   2369 <f8011510>
    3e4b:	84 c0                	test   al,al
    3e4d:	0f 84 91 08 00 00    	je     46e4 <main+0x1309>
    3e53:	0f b6 85 59 ff ff ff 	movzx  eax,BYTE PTR [rbp-0xa7]
    3e5a:	0f be c0             	movsx  eax,al
    3e5d:	89 c7                	mov    edi,eax
    3e5f:	e8 30 e5 ff ff       	call   2394 <f1083193>
    3e64:	84 c0                	test   al,al
    3e66:	0f 84 78 08 00 00    	je     46e4 <main+0x1309>
    3e6c:	0f b6 85 5a ff ff ff 	movzx  eax,BYTE PTR [rbp-0xa6]
    3e73:	0f be c0             	movsx  eax,al
    3e76:	89 c7                	mov    edi,eax
    3e78:	e8 42 e5 ff ff       	call   23bf <f2547905>
    3e7d:	84 c0                	test   al,al
    3e7f:	0f 84 5f 08 00 00    	je     46e4 <main+0x1309>
    3e85:	0f b6 85 5b ff ff ff 	movzx  eax,BYTE PTR [rbp-0xa5]
    3e8c:	0f be c0             	movsx  eax,al
    3e8f:	89 c7                	mov    edi,eax
    3e91:	e8 56 e5 ff ff       	call   23ec <f5585047>
    3e96:	84 c0                	test   al,al
    3e98:	0f 84 46 08 00 00    	je     46e4 <main+0x1309>
    3e9e:	0f b6 85 5c ff ff ff 	movzx  eax,BYTE PTR [rbp-0xa4]
    3ea5:	0f be c0             	movsx  eax,al
    3ea8:	89 c7                	mov    edi,eax
    3eaa:	e8 68 e5 ff ff       	call   2417 <f9747250>
    3eaf:	84 c0                	test   al,al
    3eb1:	0f 84 2d 08 00 00    	je     46e4 <main+0x1309>
    3eb7:	0f b6 85 5d ff ff ff 	movzx  eax,BYTE PTR [rbp-0xa3]
    3ebe:	0f be c0             	movsx  eax,al
    3ec1:	89 c7                	mov    edi,eax
    3ec3:	e8 7a e5 ff ff       	call   2442 <f2454679>
    3ec8:	84 c0                	test   al,al
    3eca:	0f 84 14 08 00 00    	je     46e4 <main+0x1309>
    3ed0:	0f b6 85 5e ff ff ff 	movzx  eax,BYTE PTR [rbp-0xa2]
    3ed7:	0f be c0             	movsx  eax,al
    3eda:	89 c7                	mov    edi,eax
    3edc:	e8 8c e5 ff ff       	call   246d <f5724032>
    3ee1:	84 c0                	test   al,al
    3ee3:	0f 84 fb 07 00 00    	je     46e4 <main+0x1309>
    3ee9:	0f b6 85 5f ff ff ff 	movzx  eax,BYTE PTR [rbp-0xa1]
    3ef0:	0f be c0             	movsx  eax,al
    3ef3:	89 c7                	mov    edi,eax
    3ef5:	e8 a0 e5 ff ff       	call   249a <f1871302>
    3efa:	84 c0                	test   al,al
    3efc:	0f 84 e2 07 00 00    	je     46e4 <main+0x1309>
    3f02:	0f b6 85 60 ff ff ff 	movzx  eax,BYTE PTR [rbp-0xa0]
    3f09:	0f be c0             	movsx  eax,al
    3f0c:	89 c7                	mov    edi,eax
    3f0e:	e8 b2 e5 ff ff       	call   24c5 <f4168763>
    3f13:	84 c0                	test   al,al
    3f15:	0f 84 c9 07 00 00    	je     46e4 <main+0x1309>
    3f1b:	0f b6 85 61 ff ff ff 	movzx  eax,BYTE PTR [rbp-0x9f]
    3f22:	0f be c0             	movsx  eax,al
    3f25:	89 c7                	mov    edi,eax
    3f27:	e8 c6 e5 ff ff       	call   24f2 <f3207138>
    3f2c:	84 c0                	test   al,al
    3f2e:	0f 84 b0 07 00 00    	je     46e4 <main+0x1309>
    3f34:	0f b6 85 62 ff ff ff 	movzx  eax,BYTE PTR [rbp-0x9e]
    3f3b:	0f be c0             	movsx  eax,al
    3f3e:	89 c7                	mov    edi,eax
    3f40:	e8 da e5 ff ff       	call   251f <f4692198>
    3f45:	84 c0                	test   al,al
    3f47:	0f 84 97 07 00 00    	je     46e4 <main+0x1309>
    3f4d:	0f b6 85 63 ff ff ff 	movzx  eax,BYTE PTR [rbp-0x9d]
    3f54:	0f be c0             	movsx  eax,al
    3f57:	89 c7                	mov    edi,eax
    3f59:	e8 ec e5 ff ff       	call   254a <f518159>
    3f5e:	84 c0                	test   al,al
    3f60:	0f 84 7e 07 00 00    	je     46e4 <main+0x1309>
    3f66:	0f b6 85 64 ff ff ff 	movzx  eax,BYTE PTR [rbp-0x9c]
    3f6d:	0f be c0             	movsx  eax,al
    3f70:	89 c7                	mov    edi,eax
    3f72:	e8 00 e6 ff ff       	call   2577 <f1762925>
    3f77:	84 c0                	test   al,al
    3f79:	0f 84 65 07 00 00    	je     46e4 <main+0x1309>
    3f7f:	0f b6 85 65 ff ff ff 	movzx  eax,BYTE PTR [rbp-0x9b]
    3f86:	0f be c0             	movsx  eax,al
    3f89:	89 c7                	mov    edi,eax
    3f8b:	e8 12 e6 ff ff       	call   25a2 <f6594036>
    3f90:	84 c0                	test   al,al
    3f92:	0f 84 4c 07 00 00    	je     46e4 <main+0x1309>
    3f98:	0f b6 85 66 ff ff ff 	movzx  eax,BYTE PTR [rbp-0x9a]
    3f9f:	0f be c0             	movsx  eax,al
    3fa2:	89 c7                	mov    edi,eax
    3fa4:	e8 26 e6 ff ff       	call   25cf <f4698560>
    3fa9:	84 c0                	test   al,al
    3fab:	0f 84 33 07 00 00    	je     46e4 <main+0x1309>
    3fb1:	0f b6 85 67 ff ff ff 	movzx  eax,BYTE PTR [rbp-0x99]
    3fb8:	0f be c0             	movsx  eax,al
    3fbb:	89 c7                	mov    edi,eax
    3fbd:	e8 38 e6 ff ff       	call   25fa <f51135>
    3fc2:	84 c0                	test   al,al
    3fc4:	0f 84 1a 07 00 00    	je     46e4 <main+0x1309>
    3fca:	0f b6 85 68 ff ff ff 	movzx  eax,BYTE PTR [rbp-0x98]
    3fd1:	0f be c0             	movsx  eax,al
    3fd4:	89 c7                	mov    edi,eax
    3fd6:	e8 4c e6 ff ff       	call   2627 <f2844159>
    3fdb:	84 c0                	test   al,al
    3fdd:	0f 84 01 07 00 00    	je     46e4 <main+0x1309>
    3fe3:	0f b6 85 69 ff ff ff 	movzx  eax,BYTE PTR [rbp-0x97]
    3fea:	0f be c0             	movsx  eax,al
    3fed:	89 c7                	mov    edi,eax
    3fef:	e8 60 e6 ff ff       	call   2654 <f5858457>
    3ff4:	84 c0                	test   al,al
    3ff6:	0f 84 e8 06 00 00    	je     46e4 <main+0x1309>
    3ffc:	0f b6 85 6a ff ff ff 	movzx  eax,BYTE PTR [rbp-0x96]
    4003:	0f be c0             	movsx  eax,al
    4006:	89 c7                	mov    edi,eax
    4008:	e8 72 e6 ff ff       	call   267f <f2731283>
    400d:	84 c0                	test   al,al
    400f:	0f 84 cf 06 00 00    	je     46e4 <main+0x1309>
    4015:	0f b6 85 6b ff ff ff 	movzx  eax,BYTE PTR [rbp-0x95]
    401c:	0f be c0             	movsx  eax,al
    401f:	89 c7                	mov    edi,eax
    4021:	e8 86 e6 ff ff       	call   26ac <f7538802>
    4026:	84 c0                	test   al,al
    4028:	0f 84 b6 06 00 00    	je     46e4 <main+0x1309>
    402e:	0f b6 85 6c ff ff ff 	movzx  eax,BYTE PTR [rbp-0x94]
    4035:	0f be c0             	movsx  eax,al
    4038:	89 c7                	mov    edi,eax
    403a:	e8 98 e6 ff ff       	call   26d7 <f3273483>
    403f:	84 c0                	test   al,al
    4041:	0f 84 9d 06 00 00    	je     46e4 <main+0x1309>
    4047:	0f b6 85 6d ff ff ff 	movzx  eax,BYTE PTR [rbp-0x93]
    404e:	0f be c0             	movsx  eax,al
    4051:	89 c7                	mov    edi,eax
    4053:	e8 aa e6 ff ff       	call   2702 <f6794679>
    4058:	84 c0                	test   al,al
    405a:	0f 84 84 06 00 00    	je     46e4 <main+0x1309>
    4060:	0f b6 85 6e ff ff ff 	movzx  eax,BYTE PTR [rbp-0x92]
    4067:	0f be c0             	movsx  eax,al
    406a:	89 c7                	mov    edi,eax
    406c:	e8 be e6 ff ff       	call   272f <f9560420>
    4071:	84 c0                	test   al,al
    4073:	0f 84 6b 06 00 00    	je     46e4 <main+0x1309>
    4079:	0f b6 85 6f ff ff ff 	movzx  eax,BYTE PTR [rbp-0x91]
    4080:	0f be c0             	movsx  eax,al
    4083:	89 c7                	mov    edi,eax
    4085:	e8 d2 e6 ff ff       	call   275c <f3026215>
    408a:	84 c0                	test   al,al
    408c:	0f 84 52 06 00 00    	je     46e4 <main+0x1309>
    4092:	0f b6 85 70 ff ff ff 	movzx  eax,BYTE PTR [rbp-0x90]
    4099:	0f be c0             	movsx  eax,al
    409c:	89 c7                	mov    edi,eax
    409e:	e8 e4 e6 ff ff       	call   2787 <f4703035>
    40a3:	84 c0                	test   al,al
    40a5:	0f 84 39 06 00 00    	je     46e4 <main+0x1309>
    40ab:	0f b6 85 71 ff ff ff 	movzx  eax,BYTE PTR [rbp-0x8f]
    40b2:	0f be c0             	movsx  eax,al
    40b5:	89 c7                	mov    edi,eax
    40b7:	e8 f8 e6 ff ff       	call   27b4 <f7480532>
    40bc:	84 c0                	test   al,al
    40be:	0f 84 20 06 00 00    	je     46e4 <main+0x1309>
    40c4:	0f b6 85 72 ff ff ff 	movzx  eax,BYTE PTR [rbp-0x8e]
    40cb:	0f be c0             	movsx  eax,al
    40ce:	89 c7                	mov    edi,eax
    40d0:	e8 0a e7 ff ff       	call   27df <f8746401>
    40d5:	84 c0                	test   al,al
    40d7:	0f 84 07 06 00 00    	je     46e4 <main+0x1309>
    40dd:	0f b6 85 73 ff ff ff 	movzx  eax,BYTE PTR [rbp-0x8d]
    40e4:	0f be c0             	movsx  eax,al
    40e7:	89 c7                	mov    edi,eax
    40e9:	e8 1c e7 ff ff       	call   280a <f1223611>
    40ee:	84 c0                	test   al,al
    40f0:	0f 84 ee 05 00 00    	je     46e4 <main+0x1309>
    40f6:	0f b6 85 74 ff ff ff 	movzx  eax,BYTE PTR [rbp-0x8c]
    40fd:	0f be c0             	movsx  eax,al
    4100:	89 c7                	mov    edi,eax
    4102:	e8 30 e7 ff ff       	call   2837 <f9386630>
    4107:	84 c0                	test   al,al
    4109:	0f 84 d5 05 00 00    	je     46e4 <main+0x1309>
    410f:	0f b6 85 75 ff ff ff 	movzx  eax,BYTE PTR [rbp-0x8b]
    4116:	0f be c0             	movsx  eax,al
    4119:	89 c7                	mov    edi,eax
    411b:	e8 44 e7 ff ff       	call   2864 <f7022724>
    4120:	84 c0                	test   al,al
    4122:	0f 84 bc 05 00 00    	je     46e4 <main+0x1309>
    4128:	0f b6 85 76 ff ff ff 	movzx  eax,BYTE PTR [rbp-0x8a]
    412f:	0f be c0             	movsx  eax,al
    4132:	89 c7                	mov    edi,eax
    4134:	e8 56 e7 ff ff       	call   288f <f6626111>
    4139:	84 c0                	test   al,al
    413b:	0f 84 a3 05 00 00    	je     46e4 <main+0x1309>
    4141:	0f b6 85 77 ff ff ff 	movzx  eax,BYTE PTR [rbp-0x89]
    4148:	0f be c0             	movsx  eax,al
    414b:	89 c7                	mov    edi,eax
    414d:	e8 6a e7 ff ff       	call   28bc <f9521409>
    4152:	84 c0                	test   al,al
    4154:	0f 84 8a 05 00 00    	je     46e4 <main+0x1309>
    415a:	0f b6 85 78 ff ff ff 	movzx  eax,BYTE PTR [rbp-0x88]
    4161:	0f be c0             	movsx  eax,al
    4164:	89 c7                	mov    edi,eax
    4166:	e8 7c e7 ff ff       	call   28e7 <f6147350>
    416b:	84 c0                	test   al,al
    416d:	0f 84 71 05 00 00    	je     46e4 <main+0x1309>
    4173:	0f b6 85 79 ff ff ff 	movzx  eax,BYTE PTR [rbp-0x87]
    417a:	0f be c0             	movsx  eax,al
    417d:	89 c7                	mov    edi,eax
    417f:	e8 90 e7 ff ff       	call   2914 <f3296195>
    4184:	84 c0                	test   al,al
    4186:	0f 84 58 05 00 00    	je     46e4 <main+0x1309>
    418c:	0f b6 85 7a ff ff ff 	movzx  eax,BYTE PTR [rbp-0x86]
    4193:	0f be c0             	movsx  eax,al
    4196:	89 c7                	mov    edi,eax
    4198:	e8 a4 e7 ff ff       	call   2941 <f5547465>
    419d:	84 c0                	test   al,al
    419f:	0f 84 3f 05 00 00    	je     46e4 <main+0x1309>
    41a5:	0f b6 85 7b ff ff ff 	movzx  eax,BYTE PTR [rbp-0x85]
    41ac:	0f be c0             	movsx  eax,al
    41af:	89 c7                	mov    edi,eax
    41b1:	e8 b6 e7 ff ff       	call   296c <f3950848>
    41b6:	84 c0                	test   al,al
    41b8:	0f 84 26 05 00 00    	je     46e4 <main+0x1309>
    41be:	0f b6 85 7c ff ff ff 	movzx  eax,BYTE PTR [rbp-0x84]
    41c5:	0f be c0             	movsx  eax,al
    41c8:	89 c7                	mov    edi,eax
    41ca:	e8 c8 e7 ff ff       	call   2997 <f8974270>
    41cf:	84 c0                	test   al,al
    41d1:	0f 84 0d 05 00 00    	je     46e4 <main+0x1309>
    41d7:	0f b6 85 7d ff ff ff 	movzx  eax,BYTE PTR [rbp-0x83]
    41de:	0f be c0             	movsx  eax,al
    41e1:	89 c7                	mov    edi,eax
    41e3:	e8 da e7 ff ff       	call   29c2 <f3371760>
    41e8:	84 c0                	test   al,al
    41ea:	0f 84 f4 04 00 00    	je     46e4 <main+0x1309>
    41f0:	0f b6 85 7e ff ff ff 	movzx  eax,BYTE PTR [rbp-0x82]
    41f7:	0f be c0             	movsx  eax,al
    41fa:	89 c7                	mov    edi,eax
    41fc:	e8 ee e7 ff ff       	call   29ef <f9565003>
    4201:	84 c0                	test   al,al
    4203:	0f 84 db 04 00 00    	je     46e4 <main+0x1309>
    4209:	0f b6 85 7f ff ff ff 	movzx  eax,BYTE PTR [rbp-0x81]
    4210:	0f be c0             	movsx  eax,al
    4213:	89 c7                	mov    edi,eax
    4215:	e8 02 e8 ff ff       	call   2a1c <f3189640>
    421a:	84 c0                	test   al,al
    421c:	0f 84 c2 04 00 00    	je     46e4 <main+0x1309>
    4222:	0f b6 45 80          	movzx  eax,BYTE PTR [rbp-0x80]
    4226:	0f be c0             	movsx  eax,al
    4229:	89 c7                	mov    edi,eax
    422b:	e8 17 e8 ff ff       	call   2a47 <f3873488>
    4230:	84 c0                	test   al,al
    4232:	0f 84 ac 04 00 00    	je     46e4 <main+0x1309>
    4238:	0f b6 45 81          	movzx  eax,BYTE PTR [rbp-0x7f]
    423c:	0f be c0             	movsx  eax,al
    423f:	89 c7                	mov    edi,eax
    4241:	e8 2c e8 ff ff       	call   2a72 <f9392038>
    4246:	84 c0                	test   al,al
    4248:	0f 84 96 04 00 00    	je     46e4 <main+0x1309>
    424e:	0f b6 45 82          	movzx  eax,BYTE PTR [rbp-0x7e]
    4252:	0f be c0             	movsx  eax,al
    4255:	89 c7                	mov    edi,eax
    4257:	e8 41 e8 ff ff       	call   2a9d <f7515979>
    425c:	84 c0                	test   al,al
    425e:	0f 84 80 04 00 00    	je     46e4 <main+0x1309>
    4264:	0f b6 45 83          	movzx  eax,BYTE PTR [rbp-0x7d]
    4268:	0f be c0             	movsx  eax,al
    426b:	89 c7                	mov    edi,eax
    426d:	e8 58 e8 ff ff       	call   2aca <f2754289>
    4272:	84 c0                	test   al,al
    4274:	0f 84 6a 04 00 00    	je     46e4 <main+0x1309>
    427a:	0f b6 45 84          	movzx  eax,BYTE PTR [rbp-0x7c]
    427e:	0f be c0             	movsx  eax,al
    4281:	89 c7                	mov    edi,eax
    4283:	e8 6f e8 ff ff       	call   2af7 <f2916766>
    4288:	84 c0                	test   al,al
    428a:	0f 84 54 04 00 00    	je     46e4 <main+0x1309>
    4290:	0f b6 45 85          	movzx  eax,BYTE PTR [rbp-0x7b]
    4294:	0f be c0             	movsx  eax,al
    4297:	89 c7                	mov    edi,eax
    4299:	e8 84 e8 ff ff       	call   2b22 <f3574708>
    429e:	84 c0                	test   al,al
    42a0:	0f 84 3e 04 00 00    	je     46e4 <main+0x1309>
    42a6:	0f b6 45 86          	movzx  eax,BYTE PTR [rbp-0x7a]
    42aa:	0f be c0             	movsx  eax,al
    42ad:	89 c7                	mov    edi,eax
    42af:	e8 99 e8 ff ff       	call   2b4d <f5319150>
    42b4:	84 c0                	test   al,al
    42b6:	0f 84 28 04 00 00    	je     46e4 <main+0x1309>
    42bc:	0f b6 45 87          	movzx  eax,BYTE PTR [rbp-0x79]
    42c0:	0f be c0             	movsx  eax,al
    42c3:	89 c7                	mov    edi,eax
    42c5:	e8 b0 e8 ff ff       	call   2b7a <f10076>
    42ca:	84 c0                	test   al,al
    42cc:	0f 84 12 04 00 00    	je     46e4 <main+0x1309>
    42d2:	0f b6 45 88          	movzx  eax,BYTE PTR [rbp-0x78]
    42d6:	0f be c0             	movsx  eax,al
    42d9:	89 c7                	mov    edi,eax
    42db:	e8 c7 e8 ff ff       	call   2ba7 <f7175572>
    42e0:	84 c0                	test   al,al
    42e2:	0f 84 fc 03 00 00    	je     46e4 <main+0x1309>
    42e8:	0f b6 45 89          	movzx  eax,BYTE PTR [rbp-0x77]
    42ec:	0f be c0             	movsx  eax,al
    42ef:	89 c7                	mov    edi,eax
    42f1:	e8 dc e8 ff ff       	call   2bd2 <f2614917>
    42f6:	84 c0                	test   al,al
    42f8:	0f 84 e6 03 00 00    	je     46e4 <main+0x1309>
    42fe:	0f b6 45 8a          	movzx  eax,BYTE PTR [rbp-0x76]
    4302:	0f be c0             	movsx  eax,al
    4305:	89 c7                	mov    edi,eax
    4307:	e8 f1 e8 ff ff       	call   2bfd <f1787361>
    430c:	84 c0                	test   al,al
    430e:	0f 84 d0 03 00 00    	je     46e4 <main+0x1309>
    4314:	0f b6 45 8b          	movzx  eax,BYTE PTR [rbp-0x75]
    4318:	0f be c0             	movsx  eax,al
    431b:	89 c7                	mov    edi,eax
    431d:	e8 06 e9 ff ff       	call   2c28 <f4506152>
    4322:	84 c0                	test   al,al
    4324:	0f 84 ba 03 00 00    	je     46e4 <main+0x1309>
    432a:	0f b6 45 8c          	movzx  eax,BYTE PTR [rbp-0x74]
    432e:	0f be c0             	movsx  eax,al
    4331:	89 c7                	mov    edi,eax
    4333:	e8 1b e9 ff ff       	call   2c53 <f8769072>
    4338:	84 c0                	test   al,al
    433a:	0f 84 a4 03 00 00    	je     46e4 <main+0x1309>
    4340:	0f b6 45 8d          	movzx  eax,BYTE PTR [rbp-0x73]
    4344:	0f be c0             	movsx  eax,al
    4347:	89 c7                	mov    edi,eax
    4349:	e8 30 e9 ff ff       	call   2c7e <f7138486>
    434e:	84 c0                	test   al,al
    4350:	0f 84 8e 03 00 00    	je     46e4 <main+0x1309>
    4356:	0f b6 45 8e          	movzx  eax,BYTE PTR [rbp-0x72]
    435a:	0f be c0             	movsx  eax,al
    435d:	89 c7                	mov    edi,eax
    435f:	e8 45 e9 ff ff       	call   2ca9 <f8239086>
    4364:	84 c0                	test   al,al
    4366:	0f 84 78 03 00 00    	je     46e4 <main+0x1309>
    436c:	0f b6 45 8f          	movzx  eax,BYTE PTR [rbp-0x71]
    4370:	0f be c0             	movsx  eax,al
    4373:	89 c7                	mov    edi,eax
    4375:	e8 5c e9 ff ff       	call   2cd6 <f4507173>
    437a:	84 c0                	test   al,al
    437c:	0f 84 62 03 00 00    	je     46e4 <main+0x1309>
    4382:	0f b6 45 90          	movzx  eax,BYTE PTR [rbp-0x70]
    4386:	0f be c0             	movsx  eax,al
    4389:	89 c7                	mov    edi,eax
    438b:	e8 71 e9 ff ff       	call   2d01 <f3890123>
    4390:	84 c0                	test   al,al
    4392:	0f 84 4c 03 00 00    	je     46e4 <main+0x1309>
    4398:	0f b6 45 91          	movzx  eax,BYTE PTR [rbp-0x6f]
    439c:	0f be c0             	movsx  eax,al
    439f:	89 c7                	mov    edi,eax
    43a1:	e8 86 e9 ff ff       	call   2d2c <f5431205>
    43a6:	84 c0                	test   al,al
    43a8:	0f 84 36 03 00 00    	je     46e4 <main+0x1309>
    43ae:	0f b6 45 92          	movzx  eax,BYTE PTR [rbp-0x6e]
    43b2:	0f be c0             	movsx  eax,al
    43b5:	89 c7                	mov    edi,eax
    43b7:	e8 9d e9 ff ff       	call   2d59 <f8149070>
    43bc:	84 c0                	test   al,al
    43be:	0f 84 20 03 00 00    	je     46e4 <main+0x1309>
    43c4:	0f b6 45 93          	movzx  eax,BYTE PTR [rbp-0x6d]
    43c8:	0f be c0             	movsx  eax,al
    43cb:	89 c7                	mov    edi,eax
    43cd:	e8 b2 e9 ff ff       	call   2d84 <f9439381>
    43d2:	84 c0                	test   al,al
    43d4:	0f 84 0a 03 00 00    	je     46e4 <main+0x1309>
    43da:	0f b6 45 94          	movzx  eax,BYTE PTR [rbp-0x6c]
    43de:	0f be c0             	movsx  eax,al
    43e1:	89 c7                	mov    edi,eax
    43e3:	e8 c7 e9 ff ff       	call   2daf <f9055518>
    43e8:	84 c0                	test   al,al
    43ea:	0f 84 f4 02 00 00    	je     46e4 <main+0x1309>
    43f0:	0f b6 45 95          	movzx  eax,BYTE PTR [rbp-0x6b]
    43f4:	0f be c0             	movsx  eax,al
    43f7:	89 c7                	mov    edi,eax
    43f9:	e8 dc e9 ff ff       	call   2dda <f9075068>
    43fe:	84 c0                	test   al,al
    4400:	0f 84 de 02 00 00    	je     46e4 <main+0x1309>
    4406:	0f b6 45 96          	movzx  eax,BYTE PTR [rbp-0x6a]
    440a:	0f be c0             	movsx  eax,al
    440d:	89 c7                	mov    edi,eax
    440f:	e8 f1 e9 ff ff       	call   2e05 <f9635223>
    4414:	84 c0                	test   al,al
    4416:	0f 84 c8 02 00 00    	je     46e4 <main+0x1309>
    441c:	0f b6 45 97          	movzx  eax,BYTE PTR [rbp-0x69]
    4420:	0f be c0             	movsx  eax,al
    4423:	89 c7                	mov    edi,eax
    4425:	e8 06 ea ff ff       	call   2e30 <f9449880>
    442a:	84 c0                	test   al,al
    442c:	0f 84 b2 02 00 00    	je     46e4 <main+0x1309>
    4432:	0f b6 45 98          	movzx  eax,BYTE PTR [rbp-0x68]
    4436:	0f be c0             	movsx  eax,al
    4439:	89 c7                	mov    edi,eax
    443b:	e8 1d ea ff ff       	call   2e5d <f9273721>
    4440:	84 c0                	test   al,al
    4442:	0f 84 9c 02 00 00    	je     46e4 <main+0x1309>
    4448:	0f b6 45 99          	movzx  eax,BYTE PTR [rbp-0x67]
    444c:	0f be c0             	movsx  eax,al
    444f:	89 c7                	mov    edi,eax
    4451:	e8 32 ea ff ff       	call   2e88 <f4577902>
    4456:	84 c0                	test   al,al
    4458:	0f 84 86 02 00 00    	je     46e4 <main+0x1309>
    445e:	0f b6 45 9a          	movzx  eax,BYTE PTR [rbp-0x66]
    4462:	0f be c0             	movsx  eax,al
    4465:	89 c7                	mov    edi,eax
    4467:	e8 47 ea ff ff       	call   2eb3 <f5841651>
    446c:	84 c0                	test   al,al
    446e:	0f 84 70 02 00 00    	je     46e4 <main+0x1309>
    4474:	0f b6 45 9b          	movzx  eax,BYTE PTR [rbp-0x65]
    4478:	0f be c0             	movsx  eax,al
    447b:	89 c7                	mov    edi,eax
    447d:	e8 5c ea ff ff       	call   2ede <f5111051>
    4482:	84 c0                	test   al,al
    4484:	0f 84 5a 02 00 00    	je     46e4 <main+0x1309>
    448a:	0f b6 45 9c          	movzx  eax,BYTE PTR [rbp-0x64]
    448e:	0f be c0             	movsx  eax,al
    4491:	89 c7                	mov    edi,eax
    4493:	e8 73 ea ff ff       	call   2f0b <f47276>
    4498:	84 c0                	test   al,al
    449a:	0f 84 44 02 00 00    	je     46e4 <main+0x1309>
    44a0:	0f b6 45 9d          	movzx  eax,BYTE PTR [rbp-0x63]
    44a4:	0f be c0             	movsx  eax,al
    44a7:	89 c7                	mov    edi,eax
    44a9:	e8 88 ea ff ff       	call   2f36 <f6350455>
    44ae:	84 c0                	test   al,al
    44b0:	0f 84 2e 02 00 00    	je     46e4 <main+0x1309>
    44b6:	0f b6 45 9e          	movzx  eax,BYTE PTR [rbp-0x62]
    44ba:	0f be c0             	movsx  eax,al
    44bd:	89 c7                	mov    edi,eax
    44bf:	e8 9d ea ff ff       	call   2f61 <f2402377>
    44c4:	84 c0                	test   al,al
    44c6:	0f 84 18 02 00 00    	je     46e4 <main+0x1309>
    44cc:	0f b6 45 9f          	movzx  eax,BYTE PTR [rbp-0x61]
    44d0:	0f be c0             	movsx  eax,al
    44d3:	89 c7                	mov    edi,eax
    44d5:	e8 b4 ea ff ff       	call   2f8e <f8761847>
    44da:	84 c0                	test   al,al
    44dc:	0f 84 02 02 00 00    	je     46e4 <main+0x1309>
    44e2:	0f b6 45 a0          	movzx  eax,BYTE PTR [rbp-0x60]
    44e6:	0f be c0             	movsx  eax,al
    44e9:	89 c7                	mov    edi,eax
    44eb:	e8 c9 ea ff ff       	call   2fb9 <f1849991>
    44f0:	84 c0                	test   al,al
    44f2:	0f 84 ec 01 00 00    	je     46e4 <main+0x1309>
    44f8:	0f b6 45 a1          	movzx  eax,BYTE PTR [rbp-0x5f]
    44fc:	0f be c0             	movsx  eax,al
    44ff:	89 c7                	mov    edi,eax
    4501:	e8 de ea ff ff       	call   2fe4 <f9094552>
    4506:	84 c0                	test   al,al
    4508:	0f 84 d6 01 00 00    	je     46e4 <main+0x1309>
    450e:	0f b6 45 a2          	movzx  eax,BYTE PTR [rbp-0x5e]
    4512:	0f be c0             	movsx  eax,al
    4515:	89 c7                	mov    edi,eax
    4517:	e8 f5 ea ff ff       	call   3011 <f217736>
    451c:	84 c0                	test   al,al
    451e:	0f 84 c0 01 00 00    	je     46e4 <main+0x1309>
    4524:	0f b6 45 a3          	movzx  eax,BYTE PTR [rbp-0x5d]
    4528:	0f be c0             	movsx  eax,al
    452b:	89 c7                	mov    edi,eax
    452d:	e8 0c eb ff ff       	call   303e <f306999>
    4532:	84 c0                	test   al,al
    4534:	0f 84 aa 01 00 00    	je     46e4 <main+0x1309>
    453a:	0f b6 45 a4          	movzx  eax,BYTE PTR [rbp-0x5c]
    453e:	0f be c0             	movsx  eax,al
    4541:	89 c7                	mov    edi,eax
    4543:	e8 23 eb ff ff       	call   306b <f7863001>
    4548:	84 c0                	test   al,al
    454a:	0f 84 94 01 00 00    	je     46e4 <main+0x1309>
    4550:	0f b6 45 a5          	movzx  eax,BYTE PTR [rbp-0x5b]
    4554:	0f be c0             	movsx  eax,al
    4557:	89 c7                	mov    edi,eax
    4559:	e8 3a eb ff ff       	call   3098 <f3462476>
    455e:	84 c0                	test   al,al
    4560:	0f 84 7e 01 00 00    	je     46e4 <main+0x1309>
    4566:	0f b6 45 a6          	movzx  eax,BYTE PTR [rbp-0x5a]
    456a:	0f be c0             	movsx  eax,al
    456d:	89 c7                	mov    edi,eax
    456f:	e8 4f eb ff ff       	call   30c3 <f2419198>
    4574:	84 c0                	test   al,al
    4576:	0f 84 68 01 00 00    	je     46e4 <main+0x1309>
    457c:	0f b6 45 a7          	movzx  eax,BYTE PTR [rbp-0x59]
    4580:	0f be c0             	movsx  eax,al
    4583:	89 c7                	mov    edi,eax
    4585:	e8 66 eb ff ff       	call   30f0 <f846584>
    458a:	84 c0                	test   al,al
    458c:	0f 84 52 01 00 00    	je     46e4 <main+0x1309>
    4592:	0f b6 45 a8          	movzx  eax,BYTE PTR [rbp-0x58]
    4596:	0f be c0             	movsx  eax,al
    4599:	89 c7                	mov    edi,eax
    459b:	e8 7b eb ff ff       	call   311b <f9397951>
    45a0:	84 c0                	test   al,al
    45a2:	0f 84 3c 01 00 00    	je     46e4 <main+0x1309>
    45a8:	0f b6 45 a9          	movzx  eax,BYTE PTR [rbp-0x57]
    45ac:	0f be c0             	movsx  eax,al
    45af:	89 c7                	mov    edi,eax
    45b1:	e8 92 eb ff ff       	call   3148 <f408757>
    45b6:	84 c0                	test   al,al
    45b8:	0f 84 26 01 00 00    	je     46e4 <main+0x1309>
    45be:	0f b6 45 aa          	movzx  eax,BYTE PTR [rbp-0x56]
    45c2:	0f be c0             	movsx  eax,al
    45c5:	89 c7                	mov    edi,eax
    45c7:	e8 a7 eb ff ff       	call   3173 <f7515021>
    45cc:	84 c0                	test   al,al
    45ce:	0f 84 10 01 00 00    	je     46e4 <main+0x1309>
    45d4:	0f b6 45 ab          	movzx  eax,BYTE PTR [rbp-0x55]
    45d8:	0f be c0             	movsx  eax,al
    45db:	89 c7                	mov    edi,eax
    45dd:	e8 bc eb ff ff       	call   319e <f5079579>
    45e2:	84 c0                	test   al,al
    45e4:	0f 84 fa 00 00 00    	je     46e4 <main+0x1309>
    45ea:	0f b6 45 ac          	movzx  eax,BYTE PTR [rbp-0x54]
    45ee:	0f be c0             	movsx  eax,al
    45f1:	89 c7                	mov    edi,eax
    45f3:	e8 d1 eb ff ff       	call   31c9 <f1334508>
    45f8:	84 c0                	test   al,al
    45fa:	0f 84 e4 00 00 00    	je     46e4 <main+0x1309>
    4600:	0f b6 45 ad          	movzx  eax,BYTE PTR [rbp-0x53]
    4604:	0f be c0             	movsx  eax,al
    4607:	89 c7                	mov    edi,eax
    4609:	e8 e8 eb ff ff       	call   31f6 <f2006371>
    460e:	84 c0                	test   al,al
    4610:	0f 84 ce 00 00 00    	je     46e4 <main+0x1309>
    4616:	0f b6 45 ae          	movzx  eax,BYTE PTR [rbp-0x52]
    461a:	0f be c0             	movsx  eax,al
    461d:	89 c7                	mov    edi,eax
    461f:	e8 ff eb ff ff       	call   3223 <f8066792>
    4624:	84 c0                	test   al,al
    4626:	0f 84 b8 00 00 00    	je     46e4 <main+0x1309>
    462c:	0f b6 45 af          	movzx  eax,BYTE PTR [rbp-0x51]
    4630:	0f be c0             	movsx  eax,al
    4633:	89 c7                	mov    edi,eax
    4635:	e8 14 ec ff ff       	call   324e <f3842174>
    463a:	84 c0                	test   al,al
    463c:	0f 84 a2 00 00 00    	je     46e4 <main+0x1309>
    4642:	0f b6 45 b0          	movzx  eax,BYTE PTR [rbp-0x50]
    4646:	0f be c0             	movsx  eax,al
    4649:	89 c7                	mov    edi,eax
    464b:	e8 2b ec ff ff       	call   327b <f1988839>
    4650:	84 c0                	test   al,al
    4652:	0f 84 8c 00 00 00    	je     46e4 <main+0x1309>
    4658:	0f b6 45 b1          	movzx  eax,BYTE PTR [rbp-0x4f]
    465c:	0f be c0             	movsx  eax,al
    465f:	89 c7                	mov    edi,eax
    4661:	e8 40 ec ff ff       	call   32a6 <f9928926>
    4666:	84 c0                	test   al,al
    4668:	74 7a                	je     46e4 <main+0x1309>
    466a:	0f b6 45 b2          	movzx  eax,BYTE PTR [rbp-0x4e]
    466e:	0f be c0             	movsx  eax,al
    4671:	89 c7                	mov    edi,eax
    4673:	e8 5b ec ff ff       	call   32d3 <f8960275>
    4678:	84 c0                	test   al,al
    467a:	74 68                	je     46e4 <main+0x1309>
    467c:	0f b6 45 b3          	movzx  eax,BYTE PTR [rbp-0x4d]
    4680:	0f be c0             	movsx  eax,al
    4683:	89 c7                	mov    edi,eax
    4685:	e8 76 ec ff ff       	call   3300 <f5663288>
    468a:	84 c0                	test   al,al
    468c:	74 56                	je     46e4 <main+0x1309>
    468e:	0f b6 45 b4          	movzx  eax,BYTE PTR [rbp-0x4c]
    4692:	0f be c0             	movsx  eax,al
    4695:	89 c7                	mov    edi,eax
    4697:	e8 8f ec ff ff       	call   332b <f1103067>
    469c:	84 c0                	test   al,al
    469e:	74 44                	je     46e4 <main+0x1309>
    46a0:	0f b6 45 b5          	movzx  eax,BYTE PTR [rbp-0x4b]
    46a4:	0f be c0             	movsx  eax,al
    46a7:	89 c7                	mov    edi,eax
    46a9:	e8 aa ec ff ff       	call   3358 <f4973817>
    46ae:	84 c0                	test   al,al
    46b0:	74 32                	je     46e4 <main+0x1309>
    46b2:	0f b6 45 b6          	movzx  eax,BYTE PTR [rbp-0x4a]
    46b6:	0f be c0             	movsx  eax,al
    46b9:	89 c7                	mov    edi,eax
    46bb:	e8 c3 ec ff ff       	call   3383 <f5477172>
    46c0:	84 c0                	test   al,al
    46c2:	74 20                	je     46e4 <main+0x1309>
    46c4:	0f b6 45 b7          	movzx  eax,BYTE PTR [rbp-0x49]
    46c8:	0f be c0             	movsx  eax,al
    46cb:	89 c7                	mov    edi,eax
    46cd:	e8 dc ec ff ff       	call   33ae <f4124796>
    46d2:	84 c0                	test   al,al
    46d4:	74 0e                	je     46e4 <main+0x1309>
    46d6:	48 8d 3d 2b 09 00 00 	lea    rdi,[rip+0x92b]        # 5008 <_IO_stdin_used+0x8>
    46dd:	e8 8e c9 ff ff       	call   1070 <puts@plt>
    46e2:	eb 0c                	jmp    46f0 <main+0x1315>
    46e4:	48 8d 3d 43 09 00 00 	lea    rdi,[rip+0x943]        # 502e <_IO_stdin_used+0x2e>
    46eb:	e8 80 c9 ff ff       	call   1070 <puts@plt>
    46f0:	90                   	nop
    46f1:	48 8b 45 f8          	mov    rax,QWORD PTR [rbp-0x8]
    46f5:	64 48 33 04 25 28 00 	xor    rax,QWORD PTR fs:0x28
    46fc:	00 00 
    46fe:	74 05                	je     4705 <main+0x132a>
    4700:	e8 7b c9 ff ff       	call   1080 <__stack_chk_fail@plt>
    4705:	c9                   	leave  
    4706:	c3                   	ret    
    4707:	66 0f 1f 84 00 00 00 	nop    WORD PTR [rax+rax*1+0x0]
    470e:	00 00 

0000000000004710 <__libc_csu_init>:
    4710:	f3 0f 1e fa          	endbr64 
    4714:	41 57                	push   r15
    4716:	4c 8d 3d 8b 46 00 00 	lea    r15,[rip+0x468b]        # 8da8 <__frame_dummy_init_array_entry>
    471d:	41 56                	push   r14
    471f:	49 89 d6             	mov    r14,rdx
    4722:	41 55                	push   r13
    4724:	49 89 f5             	mov    r13,rsi
    4727:	41 54                	push   r12
    4729:	41 89 fc             	mov    r12d,edi
    472c:	55                   	push   rbp
    472d:	48 8d 2d 7c 46 00 00 	lea    rbp,[rip+0x467c]        # 8db0 <__do_global_dtors_aux_fini_array_entry>
    4734:	53                   	push   rbx
    4735:	4c 29 fd             	sub    rbp,r15
    4738:	48 83 ec 08          	sub    rsp,0x8
    473c:	e8 bf c8 ff ff       	call   1000 <_init>
    4741:	48 c1 fd 03          	sar    rbp,0x3
    4745:	74 1f                	je     4766 <__libc_csu_init+0x56>
    4747:	31 db                	xor    ebx,ebx
    4749:	0f 1f 80 00 00 00 00 	nop    DWORD PTR [rax+0x0]
    4750:	4c 89 f2             	mov    rdx,r14
    4753:	4c 89 ee             	mov    rsi,r13
    4756:	44 89 e7             	mov    edi,r12d
    4759:	41 ff 14 df          	call   QWORD PTR [r15+rbx*8]
    475d:	48 83 c3 01          	add    rbx,0x1
    4761:	48 39 dd             	cmp    rbp,rbx
    4764:	75 ea                	jne    4750 <__libc_csu_init+0x40>
    4766:	48 83 c4 08          	add    rsp,0x8
    476a:	5b                   	pop    rbx
    476b:	5d                   	pop    rbp
    476c:	41 5c                	pop    r12
    476e:	41 5d                	pop    r13
    4770:	41 5e                	pop    r14
    4772:	41 5f                	pop    r15
    4774:	c3                   	ret    
    4775:	66 66 2e 0f 1f 84 00 	data16 nop WORD PTR cs:[rax+rax*1+0x0]
    477c:	00 00 00 00 

0000000000004780 <__libc_csu_fini>:
    4780:	f3 0f 1e fa          	endbr64 
    4784:	c3                   	ret    

Disassembly of section .fini:

0000000000004788 <_fini>:
    4788:	f3 0f 1e fa          	endbr64 
    478c:	48 83 ec 08          	sub    rsp,0x8
    4790:	48 83 c4 08          	add    rsp,0x8
    4794:	c3                   	ret    
