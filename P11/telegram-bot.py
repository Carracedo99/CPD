from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import command
import time

def ejecuta_w():
	res = command.run(['ls'])
	print(res.output)
	return str(res.output)
	
def ejecuta_ping():
	res = command.run(['ping', '-c', '1', '192.168.56.11'])
	print(res.output)
	return str(res.output)
	
def ejecuta_comando(context: ContextTypes.DEFAULT_TYPE):
	res = command.run(context.args)
	print(res.output)
	return str(res.output) 
	
def ejecuta_ping2():
	res = command.run(['ping', '-c', '1', '192.168.56.11'])
	print(res.output)
	return str(res.output)
	
async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
	await update.message.reply_text(f'Hello {update.effective_user.first_name}')
	
async def resp_ls(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
	await update.message.reply_text(ejecuta_w())
	
async def resp_ping(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
	await update.message.reply_text(ejecuta_ping())
	
async def resp_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
	await update.message.reply_text(ejecuta_comando(context))
	
async def resp_ping2(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
	await update.message.reply_text(ejecuta_ping2())

app = ApplicationBuilder().token("5984761459:AAFavzvlr1WTlzwkA7bFtjIcKhu6uK1QMOA").build()

app.add_handler(CommandHandler("hello",hello))
app.add_handler(CommandHandler("ls",resp_ls))
app.add_handler(CommandHandler("ping",resp_ping))
app.add_handler(CommandHandler("cmd",resp_cmd))
app.add_handler(CommandHandler("ping2",resp_ping2))

app.run_polling()
