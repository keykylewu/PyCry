from random import randint as r
import ast,astor
def CreateObfuscatedVarNamesList(varNamesLen):
	ForeName,EndName="",""
	for i in range(6):
		TmpRand=r(0,2)
		if TmpRand==0:
			ForeName+="I"
		elif TmpRand==1:
			ForeName+="l"
		else:
			ForeName+="T"
	for i in range(6):
		TmpRand=r(0,2)
		if TmpRand==0:
			EndName+="I"
		elif TmpRand==1:
			EndName+="l"
		else:
			EndName+="T"
	RandVarNameLen=0
	while True:
		RandVarNameLen+=1
		if 3**RandVarNameLen>=varNamesLen:
			break
	RandVarNamesList=[]
	for i in range(varNamesLen):
		while True:
			TmpRandVarName=""
			for i in range(RandVarNameLen):
				TmpRand=r(0,2)
				if TmpRand==0:
					TmpRandVarName+="I"
				elif TmpRand==1:
					TmpRandVarName+="l"
				else:
					TmpRandVarName+="T"
			if ForeName+TmpRandVarName+EndName not in RandVarNamesList:
				RandVarNamesList+=[ForeName+TmpRandVarName+EndName]
				break
	if "TmpRandVarName" in locals():
		del TmpRandVarName
	del ForeName,EndName,TmpRand
	return RandVarNamesList
def BoolObfuscator(boolObj):
	OprList=[{0:"&",1:"|",2:"^"}[r(0,2)] for i in range(8)]
	BoolList=[str(r(0,1)) for i in range(8)]
	result="("*10
	for i in range(8):
		result+=BoolList[i]+")"+OprList[i]
	CorrBool=eval(result[2:len(result)-1])
	Opr=result[::-1][0]
	if Opr=="&":
		if boolObj==True:
			if CorrBool==False:
				result+=str(r(0,1))
			else:
				result+="1"
		else:
			if CorrBool==False:
				result+=str(r(0,1))
			else:
				result+="1"
	elif Opr=="|":
		if boolObj==True:
			if CorrBool==False:
				result+="0"
			else:
				result+=str(r(0,1))
		else:
			if CorrBool==False:
				result+="0"
			else:
				result+=str(r(0,1))
	else:
		result+="0"
	result+=")"
	if boolObj==True:
		if CorrBool==False:
			result+={0:"|1",1:"^1"}[r(0,1)]
		else:
			result+={0:"&1",1:"|0",2:"|1",3:"^0"}[r(0,3)]
	else:
		if CorrBool==False:
			result+={0:"&1",1:"&0",2:"|0",3:"^0"}[r(0,3)]
		else:
			result+={0:"&0",1:"^1"}[r(0,1)]
	del CorrBool
	return result+")"
def IntObfuscator(intObj):
	MultiNumList=[2,3,5,7,11,13]
	SepIntA=r(0,intObj)
	SepIntB=intObj-SepIntA
	SepIntC,SepIntD=r(0,SepIntA),r(0,SepIntB)
	SepIntA,SepIntB,SepIntC,SepIntD=str(SepIntA-SepIntC),str(SepIntB-SepIntD),str(SepIntC),str(SepIntD)
	RandListA,RandListB,RandListC=[r(0,600),MultiNumList[r(0,5)],MultiNumList[r(0,5)]],[r(0,600),MultiNumList[r(0,5)],MultiNumList[r(0,5)]],[r(0,600),MultiNumList[r(0,5)],MultiNumList[r(0,5)]]
	RandIntAa,RandIntBa,RandIntCa=str(RandListA[0]*RandListA[1])+"*"+str(RandListA[2]),str(RandListB[0]*RandListB[1])+"*"+str(RandListB[2]),str(RandListC[0]*RandListC[1])+"*"+str(RandListC[2])
	RandIntAb,RandIntBb,RandIntCb=str(RandListA[0]*RandListA[2])+"*"+str(RandListA[1]),str(RandListB[0]*RandListB[2])+"*"+str(RandListB[1]),str(RandListC[0]*RandListC[2])+"*"+str(RandListC[1])
	del RandListA,RandListB,RandListC
	result=SepIntA+"+"+RandIntAa+"+"+SepIntB+"-"+RandIntAb+"+"+RandIntBa+"+"+SepIntC+"-"+RandIntBb+"+"+RandIntCa+"+"+SepIntD+"-"+RandIntCb
	return result
def StrObfuscator(strObj):
	StrLen=len(strObj)
	SepStrLenA=r(0,StrLen)
	SepStrLenB=StrLen-SepStrLenA
	SepStrLenC,SepStrLenD=r(0,SepStrLenA),r(0,SepStrLenB)
	SepStrLenA,SepStrLenB=SepStrLenA-SepStrLenC,SepStrLenB-SepStrLenD
	SepStrLenE,SepStrLenF,SepStrLenG,SepStrLenH=r(0,SepStrLenA),r(0,SepStrLenB),r(0,SepStrLenC),r(0,SepStrLenD)
	SepStrLenA,SepStrLenB,SepStrLenC,SepStrLenD=SepStrLenA-SepStrLenE,SepStrLenB-SepStrLenF,SepStrLenC-SepStrLenG,SepStrLenD-SepStrLenH
	SepListNum=[SepStrLenA,SepStrLenB,SepStrLenC,SepStrLenD,SepStrLenE,SepStrLenF,SepStrLenG,SepStrLenH]
	TmpSepList=[]
	ListToStrStart = 0
	for i in SepListNum:
		TmpSepList.append(strObj[ListToStrStart:ListToStrStart+i])
		ListToStrStart += i
	SepConnList=[]
	for i in range(8):
		while True:
			NewObj=r(0,7)
			if not NewObj in SepConnList:
				SepConnList+=[NewObj]
				break
	LastSepList=[None,None,None,None,None,None,None,None]
	for i in range(len(SepConnList)):
		LastSepList[SepConnList[i]]=TmpSepList[i]
	del TmpSepList
	StrLastSepList=str(LastSepList)
	del LastSepList
	result=""
	for i in range(8):
		result+=StrLastSepList+"["+str(SepConnList[i])+"]"
		if i!=7:
			result+="+"
	return result
def ObfuscateAllStr(pyCode):
	pyCode=pyCode.replace("\\\"","!__two__dot__!")
	pyCode=pyCode.replace("\\'","!__one__dot__!")
	#error_example: a='"Hello"'
	#error_example: a="'Hello'"
	SepStr=pyCode.replace("'","\"").split("\"")
	for i in range(len(SepStr)):
		if i%2==1 and (not ("!__two__dot__!" in SepStr[i])) and (not ("!__one__dot__!" in SepStr[i])):
			SepStr[i]=StrObfuscator(SepStr[i])
	result=""
	for i in range(len(SepStr)):
			result+=SepStr[i]
	result=result.replace("!__two__dot__!","\\\"").replace("\\'","!__one__dot__!")
	return result
def ReplaceAllVarName(pyCode):
	global DoneDict
	AstPyCode=ast.parse(pyCode)
	class VarNameReplacer(ast.NodeTransformer):
		def __init__(self, old_name, new_name):
			self.old_name = old_name
			self.new_name = new_name
		def visit_Name(self, node):
			if node.id == self.old_name:
				node.id = self.new_name
			return node
	class VarNameExtractor(ast.NodeVisitor):
		def __init__(self):
			self.VarNames=[]
		def visit_Name(self, node):
			self.VarNames+=[node.id]
			self.generic_visit(node)
	def GetImports(pyCode):
		tree = ast.parse(pyCode)
		Imports=[]
		FromImports=[]
		Imports = [node.names[0].name for node in ast.walk(tree) if isinstance(node, ast.Import) for name in node.names]
		for node in [node for node in tree.body if isinstance(node, ast.ImportFrom)]:
			FromImports =[name.name if name.asname is None else name.asname for name in node.names]
		return Imports+FromImports
	Extractor = VarNameExtractor()
	Extractor.visit(AstPyCode)
	VarNames=Extractor.VarNames
	del Extractor
	VarNames=list(set(VarNames))
	VarNames=[x for x in VarNames if x not in ['ArithmeticError', 'AssertionError', 'AttributeError', 'BaseException', 'BlockingIOError', 'BrokenPipeError', 'BufferError', 'BytesWarning', 'ChildProcessError', 'ConnectionAbortedError', 'ConnectionError', 'ConnectionRefusedError', 'ConnectionResetError', 'DeprecationWarning', 'EOFError', 'Ellipsis', 'EnvironmentError', 'Exception', 'False', 'FileExistsError', 'FileNotFoundError', 'FloatingPointError', 'FutureWarning', 'GeneratorExit', 'IOError', 'ImportError', 'ImportWarning', 'IndentationError', 'IndexError', 'InterruptedError', 'IsADirectoryError', 'KeyError', 'KeyboardInterrupt', 'LookupError', 'MemoryError', 'ModuleNotFoundError', 'NameError', 'None', 'NotADirectoryError', 'NotImplemented', 'NotImplementedError', 'OSError', 'OverflowError', 'PendingDeprecationWarning', 'PermissionError', 'ProcessLookupError', 'RecursionError', 'ReferenceError', 'ResourceWarning', 'RuntimeError', 'RuntimeWarning', 'StopAsyncIteration', 'StopIteration', 'SyntaxError', 'SyntaxWarning', 'SystemError', 'SystemExit', 'TabError', 'TimeoutError', 'True', 'TypeError', 'UnboundLocalError', 'UnicodeDecodeError', 'UnicodeEncodeError', 'UnicodeError', 'UnicodeTranslateError', 'UnicodeWarning', 'UserWarning', 'ValueError', 'Warning', 'WindowsError', 'ZeroDivisionError', '__build_class__', '__debug__', '__doc__', '__import__', '__loader__', '__name__', '__package__', '__spec__', 'abs', 'all', 'any', 'ascii', 'bin', 'bool', 'breakpoint', 'bytearray', 'bytes', 'callable', 'chr', 'classmethod', 'compile', 'complex', 'copyright', 'credits', 'delattr', 'dict', 'dir', 'divmod', 'enumerate', 'eval', 'exec', 'exit', 'filter', 'float', 'format', 'frozenset', 'getattr', 'globals', 'hasattr', 'hash', 'help', 'hex', 'id', 'input', 'int', 'isinstance', 'issubclass', 'iter', 'len', 'license', 'list', 'locals', 'map', 'max', 'memoryview', 'min', 'next', 'object', 'oct', 'open', 'ord', 'pow', 'print', 'property', 'quit', 'range', 'repr', 'reversed', 'round', 'set', 'setattr', 'slice', 'sorted', 'staticmethod', 'str', 'sum', 'super', 'tuple', 'type', 'vars', 'zip']]
	VarNames=[x for x in VarNames if x not in GetImports(pyCode)]
	RandVarNamesList=CreateObfuscatedVarNamesList(len(VarNames))
	DoneDict={}
	for i in range(len(RandVarNamesList)):
		DoneDict[VarNames[i]]=RandVarNamesList[i]
		Replacer=VarNameReplacer(VarNames[i],RandVarNamesList[i])
		AstPyCode=Replacer.visit(AstPyCode)
	result=astor.to_source(AstPyCode)
	return result
def ObfuscateArgu(pyCode):
	class ParameterRenamer(ast.NodeTransformer):
		def visit_FunctionDef(self, node):
			self.generic_visit(node)
			for arg in node.args.args:
				arg.arg=DoneDict[arg.arg]
			return node
	Tree = ast.parse(pyCode)
	Renamer = ParameterRenamer()
	ObfuscatedTree = Renamer.visit(Tree)
	ObfuscatedPyCode = astor.to_source(ObfuscatedTree)
	return ObfuscatedPyCode
def ObfuscateClass(pyCode):
	Tree = ast.parse(pyCode)
	for node in ast.walk(Tree):
		if isinstance(node, ast.ClassDef):
			node.name = DoneDict[node.name]
	NewCode = astor.to_source(Tree)
	return NewCode
def ObfuscateAllInt(pyCode):
	AstPyCode=ast.parse(pyCode)
	class IntReplacer(ast.NodeTransformer):
		def visit_Num(self, node):
			Value = IntObfuscator(node.n)
			return ast.copy_location(ast.parse(Value).body[0].value, node)
	Replacer=IntReplacer()
	result=astor.to_source(Replacer.visit(AstPyCode))
	del Replacer
	return result
def ObfuscateAllBool(pyCode):
	AstPyCode=ast.parse(pyCode)
	class ObfuscateBoolTransformer(ast.NodeTransformer):
		def visit_Constant(self, node):
			if isinstance(node.value, bool):
				return ast.Call(func=ast.Name(id='bool', ctx=ast.Load()),args=[ast.parse(BoolObfuscator(node.value))],keywords=[])
	Transformer=ObfuscateBoolTransformer()
	result=astor.to_source(Transformer.visit(AstPyCode))
	return result
def RunObfuscater(pyCode):
	pyCode=ReplaceAllVarName(pyCode)
	pyCode=ObfuscateArgu(pyCode)
	pyCode=ObfuscateClass(pyCode)
	pyCode=ObfuscateAllInt(pyCode)
	pyCode=ObfuscateAllBool(pyCode)
	pyCode=ObfuscateAllStr(pyCode)
	return pyCode



print(RunObfuscater('''
if True:
	print(False)
else:
	print(True)
'''))