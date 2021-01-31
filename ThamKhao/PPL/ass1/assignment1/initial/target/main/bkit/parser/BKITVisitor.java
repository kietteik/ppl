// Generated from main/bkit/parser/BKIT.g4 by ANTLR 4.7.2
import org.antlr.v4.runtime.tree.ParseTreeVisitor;

/**
 * This interface defines a complete generic visitor for a parse tree produced
 * by {@link BKITParser}.
 *
 * @param <T> The return type of the visit operation. Use {@link Void} for
 * operations with no return type.
 */
public interface BKITVisitor<T> extends ParseTreeVisitor<T> {
	/**
	 * Visit a parse tree produced by {@link BKITParser#program}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitProgram(BKITParser.ProgramContext ctx);
	/**
	 * Visit a parse tree produced by {@link BKITParser#listVarDeclar}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitListVarDeclar(BKITParser.ListVarDeclarContext ctx);
	/**
	 * Visit a parse tree produced by {@link BKITParser#listFuncDeclar}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitListFuncDeclar(BKITParser.ListFuncDeclarContext ctx);
	/**
	 * Visit a parse tree produced by {@link BKITParser#noNullListVarDeclar}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitNoNullListVarDeclar(BKITParser.NoNullListVarDeclarContext ctx);
	/**
	 * Visit a parse tree produced by {@link BKITParser#noNullListFuncDeclar}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitNoNullListFuncDeclar(BKITParser.NoNullListFuncDeclarContext ctx);
	/**
	 * Visit a parse tree produced by {@link BKITParser#vardeclara}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitVardeclara(BKITParser.VardeclaraContext ctx);
	/**
	 * Visit a parse tree produced by {@link BKITParser#listvar}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitListvar(BKITParser.ListvarContext ctx);
	/**
	 * Visit a parse tree produced by {@link BKITParser#var}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitVar(BKITParser.VarContext ctx);
	/**
	 * Visit a parse tree produced by {@link BKITParser#nonInitVar}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitNonInitVar(BKITParser.NonInitVarContext ctx);
	/**
	 * Visit a parse tree produced by {@link BKITParser#initVar}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitInitVar(BKITParser.InitVarContext ctx);
	/**
	 * Visit a parse tree produced by {@link BKITParser#varArrayIdentifier}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitVarArrayIdentifier(BKITParser.VarArrayIdentifierContext ctx);
	/**
	 * Visit a parse tree produced by {@link BKITParser#var_index_operators}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitVar_index_operators(BKITParser.Var_index_operatorsContext ctx);
	/**
	 * Visit a parse tree produced by {@link BKITParser#literal}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitLiteral(BKITParser.LiteralContext ctx);
	/**
	 * Visit a parse tree produced by {@link BKITParser#funcdeclara}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitFuncdeclara(BKITParser.FuncdeclaraContext ctx);
	/**
	 * Visit a parse tree produced by {@link BKITParser#listparam}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitListparam(BKITParser.ListparamContext ctx);
	/**
	 * Visit a parse tree produced by {@link BKITParser#param}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitParam(BKITParser.ParamContext ctx);
	/**
	 * Visit a parse tree produced by {@link BKITParser#funcbody}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitFuncbody(BKITParser.FuncbodyContext ctx);
	/**
	 * Visit a parse tree produced by {@link BKITParser#liststatements}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitListstatements(BKITParser.ListstatementsContext ctx);
	/**
	 * Visit a parse tree produced by {@link BKITParser#noNullListStatements}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitNoNullListStatements(BKITParser.NoNullListStatementsContext ctx);
	/**
	 * Visit a parse tree produced by {@link BKITParser#statement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitStatement(BKITParser.StatementContext ctx);
	/**
	 * Visit a parse tree produced by {@link BKITParser#assigment}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitAssigment(BKITParser.AssigmentContext ctx);
	/**
	 * Visit a parse tree produced by {@link BKITParser#if_statement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitIf_statement(BKITParser.If_statementContext ctx);
	/**
	 * Visit a parse tree produced by {@link BKITParser#for_statement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitFor_statement(BKITParser.For_statementContext ctx);
	/**
	 * Visit a parse tree produced by {@link BKITParser#while_statement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitWhile_statement(BKITParser.While_statementContext ctx);
	/**
	 * Visit a parse tree produced by {@link BKITParser#do_while_statement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitDo_while_statement(BKITParser.Do_while_statementContext ctx);
	/**
	 * Visit a parse tree produced by {@link BKITParser#break_statement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitBreak_statement(BKITParser.Break_statementContext ctx);
	/**
	 * Visit a parse tree produced by {@link BKITParser#continue_statement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitContinue_statement(BKITParser.Continue_statementContext ctx);
	/**
	 * Visit a parse tree produced by {@link BKITParser#call_statement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitCall_statement(BKITParser.Call_statementContext ctx);
	/**
	 * Visit a parse tree produced by {@link BKITParser#return_statement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitReturn_statement(BKITParser.Return_statementContext ctx);
	/**
	 * Visit a parse tree produced by {@link BKITParser#exp}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitExp(BKITParser.ExpContext ctx);
	/**
	 * Visit a parse tree produced by {@link BKITParser#exp1}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitExp1(BKITParser.Exp1Context ctx);
	/**
	 * Visit a parse tree produced by {@link BKITParser#exp2}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitExp2(BKITParser.Exp2Context ctx);
	/**
	 * Visit a parse tree produced by {@link BKITParser#exp3}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitExp3(BKITParser.Exp3Context ctx);
	/**
	 * Visit a parse tree produced by {@link BKITParser#exp4}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitExp4(BKITParser.Exp4Context ctx);
	/**
	 * Visit a parse tree produced by {@link BKITParser#exp5}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitExp5(BKITParser.Exp5Context ctx);
	/**
	 * Visit a parse tree produced by {@link BKITParser#exp6}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitExp6(BKITParser.Exp6Context ctx);
	/**
	 * Visit a parse tree produced by {@link BKITParser#exp7}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitExp7(BKITParser.Exp7Context ctx);
	/**
	 * Visit a parse tree produced by {@link BKITParser#element_exp}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitElement_exp(BKITParser.Element_expContext ctx);
	/**
	 * Visit a parse tree produced by {@link BKITParser#index_operators}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitIndex_operators(BKITParser.Index_operatorsContext ctx);
	/**
	 * Visit a parse tree produced by {@link BKITParser#func_call}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitFunc_call(BKITParser.Func_callContext ctx);
	/**
	 * Visit a parse tree produced by {@link BKITParser#listExp}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitListExp(BKITParser.ListExpContext ctx);
	/**
	 * Visit a parse tree produced by {@link BKITParser#noNullListExp}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitNoNullListExp(BKITParser.NoNullListExpContext ctx);
}