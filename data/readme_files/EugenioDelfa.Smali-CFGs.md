Smali-CFGs
==========

Smali Control Flow Graph's

Package Usage by Application.

	(ed@CFGCli) > !pu Ljavax/crypto
	*  Analized Application uses the next Ljavax/crypto Methods:
		 · BadPaddingException;->getMessage()Ljava/lang/String;
		 · BadPaddingException;->toString()Ljava/lang/String;
		 · Cipher;->doFinal([B)[B
		 · Cipher;->getInstance(Ljava/lang/String;)Ljavax/crypto/Cipher;
		 · Cipher;->init(ILjava/security/Key;)V
		 · Cipher;->init(ILjava/security/Key;Ljava/security/spec/AlgorithmParameterSpec;)V
		 · CipherInputStream;-><init>(Ljava/io/InputStream;Ljavax/crypto/Cipher;)V
		 · CipherInputStream;->read([B)I
		 · CipherOutputStream;-><init>(Ljava/io/OutputStream;Ljavax/crypto/Cipher;)V
		 · IllegalBlockSizeException;->getMessage()Ljava/lang/String;
		 · IllegalBlockSizeException;->toString()Ljava/lang/String;
		 · KeyGenerator;->generateKey()Ljavax/crypto/SecretKey;
		 · KeyGenerator;->getInstance(Ljava/lang/String;)Ljavax/crypto/KeyGenerator;
		 · KeyGenerator;->init(I)V
		 · NoSuchPaddingException;->getMessage()Ljava/lang/String;
		 · NoSuchPaddingException;->toString()Ljava/lang/String;
		 · SecretKey;->getEncoded()[B
		 · SecretKeyFactory;->generateSecret(Ljava/security/spec/KeySpec;)Ljavax/crypto/SecretKey;
		 · SecretKeyFactory;->getInstance(Ljava/lang/String;)Ljavax/crypto/SecretKeyFactory;
		 · spec/DESKeySpec;-><init>([B)V
		 · spec/IvParameterSpec;-><init>([B)V
		 · spec/PBEKeySpec;-><init>([C)V
		 · spec/PBEKeySpec;-><init>([C[BI)V
		 · spec/PBEParameterSpec;-><init>([BI)V
		 · spec/SecretKeySpec;-><init>([BLjava/lang/String;)V

Single Cross-References (2 depth level).

	(ed@CFGCli) > !xf --max_levels 2 --direction 2 "Ljavax/crypto/Cipher;->doFinal([B)[B"
	*  Cross-References with a 2 recursion level.

![](https://raw.github.com/EugenioDelfa/Smali-CFGs/master/imgs/CrossReferences.png)


Global string search.

	(ed@CFGCli) > !sp _key
	· String Patterns ['_key'] have been located at above Application Methods:
		 · Lcom/vvt/appengine/exec/ExecGetSettings;->createSettingsObject(Lcom/vvt/appengine/AppEngineComponent;ILjava/util/List;)Lcom/vvt/remotecontrol/output/RmtCtrlOutputSettings;
		 · Lcom/vvt/appengine/AppEngineHelper$2;-><clinit>()V
		 · Lcom/vvt/phoenix/prot/session/SessionManager;->updateSession(Lcom/vvt/phoenix/prot/session/SessionInfo;)Z
		 · Lcom/vvt/callmanager/ref/BugEngine;->setSmsInterceptForMonitorNumber(Ljava/util/List;)V
		 · Lcom/vvt/base/security/FxSecurityUrl;->encrypt([BZ)[B
		 · Lcom/vvt/appengine/AppEngine;->removeDownloadSmsAndRemoteCommands()V
		 · Lcom/vvt/appengine/AppEngine;-><clinit>()V
		 · Lcom/vvt/appengine/AppEngine;->removeBrowserHistory()V
		 · Lcom/vvt/remotecommand/processor/troubleshoot/ProcRequestSettings;->createMessage(Lcom/vvt/remotecontrol/output/RmtCtrlOutputSettings;Ljava/util/List;ZZ)Ljava/lang/String;
		 · Lcom/vvt/base/security/FxSecurity;->decrypt([BZ)[B
		 · Lcom/vvt/capture/facebook/daemon/FacebookDatabaseHelper;->getUserProfile(Landroid/database/sqlite/SQLiteDatabase;Ljava/lang/String;)[B
		 · Lcom/vvt/phoenix/prot/CommandServiceManager;->onAsyncCallbackInvoked(Lcom/vvt/phoenix/prot/CommandListener;I[Ljava/lang/Object;)V
		 · Lcom/vvt/appengine/exec/ExecManageCommonData;->getFeatureStringWord(Lcom/vvt/base/FeatureId;)Ljava/lang/String;
		 · Lcom/vvt/base/FeatureId;-><clinit>()V
		 · Lcom/vvt/phoenix/prot/session/SessionManager;->persistSession(Lcom/vvt/phoenix/prot/session/SessionInfo;)Z
		 · Lcom/vvt/base/security/FxSecurity;->getConstant([B)Ljava/lang/String;
		 · Lcom/vvt/remotecommand/processor/misc/ProcSetSettings$1;-><clinit>()V
		 · Lcom/vvt/capture/line/LineCapturingHelper;->getStickerAttachment(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)Ljava/util/ArrayList;
		 · Lcom/vvt/appengine/exec/ExecManageCommonData$1;-><clinit>()V
		 · Lcom/vvt/remotecommand/processor/misc/ManageCommonDataConstant$CommonData$7;->getFeatureId()Lcom/vvt/base/FeatureId;
		 · Lcom/vvt/base/security/FxSecurityUrl;->decrypt([BZ)[B
		 · Lcom/vvt/phoenix/prot/session/SessionManager;->extractSessionFromDbRow(Landroid/database/Cursor;Lcom/vvt/phoenix/prot/session/SessionInfo;)V
		 · Lcom/vvt/remotecommand/processor/misc/ManageCommonDataConstant$CommonData$6;->getFeatureId()Lcom/vvt/base/FeatureId;
		 · Lcom/vvt/phoenix/prot/session/SessionManager;->openOrCreateSessionDatabase()V
		 · Lcom/vvt/remotecommand/SetSettingsConstant;->getFeatureId(I)Lcom/vvt/base/FeatureId;
		 · Lcom/vvt/phoenix/prot/session/SessionManager;->upgradeDatabase(I)V
		 · Lcom/vvt/remotecommand/processor/misc/ManageCommonDataConstant;-><clinit>()V
		 · Lcom/vvt/capture/facebook/daemon/FacebookDatabaseHelper;->getParticipant(Landroid/database/sqlite/SQLiteDatabase;Ljava/lang/String;Ljava/lang/String;Lcom/vvt/im/events/info/OwnerInfo;)Ljava/util/List;
		 · Lcom/vvt/base/security/FxSecurityUrl;->getConstant([B)Ljava/lang/String;
		 · Lcom/vvt/appengine/AppEngine;->removeDownloads()V
		 · Lcom/vvt/base/security/FxSecurity;->encrypt([BZ)[B
		 · Lcom/vvt/appengine/AppEngineHelper;->manageKeywords(Lcom/vvt/appengine/AppEngineComponent;Ljava/util/List;Z)V
		 · Lcom/vvt/remotecommand/processor/misc/ManageCommonDataConstant$CommonData$8;->getFeatureId()Lcom/vvt/base/FeatureId;
		 · Lcom/vvt/capture/facebook/daemon/FacebookDatabaseHelper;->getSenderInfo(Landroid/database/sqlite/SQLiteDatabase;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)Lcom/vvt/im/events/info/SenderInfo;
		 · Lcom/vvt/appengine/exec/ExecSendSettingsEvent;->createSettingsEvent(Lcom/vvt/remotecontrol/output/RmtCtrlOutputSettings;Ljava/util/List;)Lcom/vvt/events/FxSettingEvent;
		 · Lcom/vvt/remotecommand/processor/misc/ManageCommonDataConstant$CommonData;-><clinit>()V
		 · Lcom/vvt/base/security/FxSecurityUrl;-><clinit>()V
		 · Lcom/vvt/base/security/FxSecurity;-><clinit>()V
		 · Lcom/vvt/remotecommand/processor/misc/ProcManageCommonData;->process(Lcom/vvt/remotecommand/RemoteCommand;Lcom/vvt/remotecommand/processor/RemoteCommandListener;)V
		 · Lcom/vvt/remotecommand/processor/misc/ManageCommonDataConstant$CommonData$5;->getFeatureId()Lcom/vvt/base/FeatureId;
		 · Lcom/vvt/appengine/exec/ExecGetSettings$1;-><clinit>()V
		 · Lcom/vvt/base/security/Constant;-><clinit>()V

Full Cross-References marking string matches.

	(ed@CFGCli) > !xf --max_levels 6 --direction 0 --str_reg _key "Ljavax/crypto/Cipher;->doFinal([B)[B"
	*  Cross-References with a 6 recursion level and String Pattern search.
		 - Lcom/vvt/base/security/FxSecurity;->decrypt([BZ)[B
			 - sget-object v6, Lcom/vvt/base/security/FxSecurity;->MASTER_KEY:[B
			 - sget-object v6, Lcom/vvt/base/security/FxSecurity;->CHECKSUM_KEY:[B
			 - sget-object v6, Lcom/vvt/base/security/FxSecurity;->DYNAMIC_KEY:[B
		 - Lcom/vvt/base/security/FxSecurity;->getConstant([B)Ljava/lang/String;
			 - sget-object v6, Lcom/vvt/base/security/FxSecurity;->MASTER_KEY:[B
			 - sget-object v6, Lcom/vvt/base/security/FxSecurity;->CONSTANT_KEY:[B
		 - Lcom/vvt/base/security/FxSecurityUrl;->getConstant([B)Ljava/lang/String;
			 - sget-object v6, Lcom/vvt/base/security/FxSecurityUrl;->MASTER_KEY:[B
			 - sget-object v6, Lcom/vvt/base/security/FxSecurityUrl;->CONSTANT_KEY:[B
		 - Lcom/vvt/base/security/FxSecurityUrl;->encrypt([BZ)[B
			 - sget-object v5, Lcom/vvt/base/security/FxSecurityUrl;->MASTER_KEY:[B
			 - sget-object v5, Lcom/vvt/base/security/FxSecurityUrl;->CHECKSUM_KEY:[B
			 - sget-object v5, Lcom/vvt/base/security/FxSecurityUrl;->DYNAMIC_KEY:[B
		 - Lcom/vvt/base/security/FxSecurity;->encrypt([BZ)[B
			 - sget-object v6, Lcom/vvt/base/security/FxSecurity;->MASTER_KEY:[B
			 - sget-object v6, Lcom/vvt/base/security/FxSecurity;->CHECKSUM_KEY:[B
			 - sget-object v6, Lcom/vvt/base/security/FxSecurity;->DYNAMIC_KEY:[B
		 - Lcom/vvt/base/security/FxSecurityUrl;->decrypt([BZ)[B
			 - sget-object v5, Lcom/vvt/base/security/FxSecurityUrl;->MASTER_KEY:[B
			 - sget-object v5, Lcom/vvt/base/security/FxSecurityUrl;->CHECKSUM_KEY:[B
			 - sget-object v5, Lcom/vvt/base/security/FxSecurityUrl;->DYNAMIC_KEY:[B

![](https://raw.github.com/EugenioDelfa/Smali-CFGs/master/imgs/CrossReferencesWithPatterns.png)

Which code lines match:

	(ed@CFGCli) > !sp -m "Lcom/vvt/base/security/FxSecurity;->getConstant([B)Ljava/lang/String;" _key
	· String Patterns ['_key'] matches at Lcom/vvt/base/security/FxSecurity;->getConstant([B)Ljava/lang/String; are:
		 · sget-object v6, Lcom/vvt/base/security/FxSecurity;->MASTER_KEY:[B
		 · sget-object v6, Lcom/vvt/base/security/FxSecurity;->CONSTANT_KEY:[B


How method seems without out calls:

	(ed@CFGCli) > !if "Lcom/vvt/base/security/FxSecurity;->getConstant([B)Ljava/lang/String;"
	*  Method Lcom/vvt/base/security/FxSecurity;->getConstant([B)Ljava/lang/String; Instructions Flow saved to MethodInstructionsFlow.png.

![](https://raw.github.com/EugenioDelfa/Smali-CFGs/master/imgs/MethodInstructionsFlow_single.png)

And with out calls:

	(ed@CFGCli) > !if -f "Lcom/vvt/base/security/FxSecurity;->getConstant([B)Ljava/lang/String;"
	*  Method Lcom/vvt/base/security/FxSecurity;->getConstant([B)Ljava/lang/String; Instructions Flow saved to MethodInstructionsFlow2.png.

![](https://raw.github.com/EugenioDelfa/Smali-CFGs/master/imgs/MethodInstructionsFlow_full.png)
