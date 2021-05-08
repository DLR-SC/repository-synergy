Postmortem Analysis for lldb

largely ported from [mdb
v8](https://github.com/joyent/node/tree/master/deps/mdb_v8)


---


```bash
git clone git://github.com/tjfontaine/lldb-v8
lldb -c ./path/to/core $(which node)
(lldb) command script import /path/to/lldb-v8/v8.py
Identified version: 3.14.5.9
(lldb) js<tab>
Available completions:
  jsframe
  jsprint
  jsstack
  jstype
(lldb) jsstack
thread #0
  frame #0: 0x0000009226e952 libsystem_kernel.dylib`__pthread_kill + 10
  frame #1: 0x0000009582d167 libsystem_pthread.dylib`pthread_kill + 101
  frame #2: 0x0000009ab9229c libsystem_c.dylib`abort + 155
  frame #3: 0x0000000041ebcd node`node::Abort(v8::Arguments const&) at node.cc:1348 ((const v8::Arguments &)args=0xbffff3b0)
  frame #4: 0x0000000015aba7 node`v8::internal::Builtin_HandleApiCall(v8::internal::(anonymous namespace)::BuiltinArguments<(v8::internal::BuiltinExtraArguments)1>, v8::internal::Isolate*) at builtins.cc:1146 ((v8::internal::(anonymous namespace)::HandleApiCallArgumentsType)args=None, (v8::internal::Isolate *)isolate=0x01211400)
  frame #5: 0x000000bffff414 internal (Code: 0x0000004be0a301)
  frame #6: 0x000000bffff430 <anonymous (as anon)>
  frame #7: 0x000000bffff44c <InternalFrame>
  frame #8: 0x000000bffff488 <EntryFrame>
  frame #9: 0x0000000018d6f2 node`v8::internal::Invoke(bool, v8::internal::Handle<v8::internal::JSFunction>, v8::internal::Handle<v8::internal::Object>, int, v8::internal::Handle<v8::internal::Object>*, bool*) at execution.cc:118 ((bool)is_construct=None, (v8::internal::Handle<v8::internal::JSFunction>)function=None, (v8::internal::Handle<v8::internal::Object>)receiver=None, (int)argc=None, (v8::internal::Handle<v8::internal::Object> *)args=None, (bool *)has_pending_exception=None)
  frame #10: 0x0000000018d23b node`v8::internal::Execution::Call(v8::internal::Handle<v8::internal::Object>, v8::internal::Handle<v8::internal::Object>, int, v8::internal::Handle<v8::internal::Object>*, bool*, bool) at execution.cc:166 ((v8::internal::Handle<v8::internal::Object>)callable=None, (v8::internal::Handle<v8::internal::Object>)receiver=None, (int)argc=None, (v8::internal::Handle<v8::internal::Object> *)argv=None, (bool *)pending_exception=0xbffff56f, (bool)convert_receiver=None)
  frame #11: 0x000000001221f1 node`v8::Script::Run() at api.cc:1620 ((v8::Script *)this=None)
  frame #12: 0x00000000434bb4 node`v8::Handle<v8::Value> node::WrappedScript::EvalMachine<(node::WrappedScript::EvalInputFlags)0, (node::WrappedScript::EvalContextFlags)0, (node::WrappedScript::EvalOutputFlags)0>(v8::Arguments const&) at node_script.cc:418 ((const v8::Arguments &)args=0x00000009)
  frame #13: 0x0000000015aba7 node`v8::internal::Builtin_HandleApiCall(v8::internal::(anonymous namespace)::BuiltinArguments<(v8::internal::BuiltinExtraArguments)1>, v8::internal::Isolate*) at builtins.cc:1146 ((v8::internal::(anonymous namespace)::HandleApiCallArgumentsType)args=None, (v8::internal::Isolate *)isolate=0x01211400)
  frame #14: 0x000000bffff6bc internal (Code: 0x0000004be0a301)
  frame #15: 0x000000bffff6e0 <anonymous (as anon)> (0x3a735629 [JSObject], 0x3a7365b5 [JSFunction], 0x3a7355ad [JSObject], 0x3a7364e9 [ConsString], 0x5fc0c401 [SeqAsciiString])
  frame #16: 0x000000bffff714 <InternalFrame>
  frame #17: 0x000000bffff74c <anonymous (as Module._compile)> (0x3a73665d [SeqAsciiString], 0x3a7364e9 [ConsString])
  frame #18: 0x000000bffff784 <evalScript> (0x5fc14ff1 [SeqAsciiString])
  frame #19: 0x000000bffff7c0 <startup>
  frame #20: 0x000000bffff7dc <anonymous (as anon)> (0x3a708bf1 [JSObject])
  frame #21: 0x000000bffff7fc <InternalFrame>
  frame #22: 0x000000bffff838 <EntryFrame>
  frame #23: 0x0000000018d6f2 node`v8::internal::Invoke(bool, v8::internal::Handle<v8::internal::JSFunction>, v8::internal::Handle<v8::internal::Object>, int, v8::internal::Handle<v8::internal::Object>*, bool*) at execution.cc:118 ((bool)is_construct=None, (v8::internal::Handle<v8::internal::JSFunction>)function=None, (v8::internal::Handle<v8::internal::Object>)receiver=None, (int)argc=None, (v8::internal::Handle<v8::internal::Object> *)args=None, (bool *)has_pending_exception=None)
  frame #24: 0x0000000018d23b node`v8::internal::Execution::Call(v8::internal::Handle<v8::internal::Object>, v8::internal::Handle<v8::internal::Object>, int, v8::internal::Handle<v8::internal::Object>*, bool*, bool) at execution.cc:166 ((v8::internal::Handle<v8::internal::Object>)callable=None, (v8::internal::Handle<v8::internal::Object>)receiver=None, (int)argc=None, (v8::internal::Handle<v8::internal::Object> *)argv=None, (bool *)pending_exception=0xbffff92b, (bool)convert_receiver=None)
  frame #25: 0x00000000131c4e node`v8::Function::Call(v8::Handle<v8::Object>, int, v8::Handle<v8::Value>*) at api.cc:3667 ((v8::Function *)this=None, (v8::Handle<v8::Object>)recv=None, (int)argc=None, (v8::Handle<v8::Value> *)argv=None)
  frame #26: 0x000000004200a1 node`node::Load(v8::Handle<v8::Object>) at node.cc:2496 ((v8::Handle<v8::Object>)process_l=None)
  frame #27: 0x00000000420e14 node`node::Start(int, char**) at node.cc:3086 ((int)argc=None, (char **)argv=0x00c465e0)
  frame #28: 0x00000000001e35 node`start + 53
```
