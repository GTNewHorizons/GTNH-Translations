<NoInclude>
  # Machine Property template

  ## Params
  | name | type | details |
  | --- | --- | --- |
  | tier | `string` | Unlock tier for machine |
  | size | `string` | Size for machine(LxWxH). can use `Varies` to present resizable machines |
  | power | `PowerEnum?` | Energy/Dynamo hatch restriction. default="regular" |
  | oc | `OCEnum?` | Overclock property. default="imperfect" |
  | reqMaintenance | `boolean?` | Maintenance Required, default=false |
  | pollution | `number?` | Pollution machine generates by gibbl/s. default=no pollution |
  | reqMuffler | `boolean?` | Muffler hatch required, default=false |

  ## Type
  ### PowerEnum
  - `regular`: Regular
  - `any`: Any Hatches allowed, includes Multi-Amp and Laser Hatches
  - `unlockable`: Regular, but upgrading tier can unlock restrictions
  - `none`: None
  - `under4a`: Lower than 4A
  - `varies`: Varies

  ### OCEnum 
  - `imperfect`: Imperfect
  - `perfect`: Perfect
  - `unique`: Unique
  - `none`: None
  - `mixed`: Mixed
  - `varies`: Varies

  ## Examples
  ```mdx
  <Template name="properties"
    tier="MV"
    size="10x10x10"
    reqMaintenance
    pollution="100"
    reqMuffler
  />
  ```
</NoInclude>

<IncludeOnly>
  <table>
    <thead><tr><th>Property</th><th>Details</th></tr></thead>
    <tbody>
      <tr><td>Unlock Tier</td><td><Param name="tier">&cNo Tier Provided&r</Param></td></tr>
      
      <tr><td>Structure Size(LxWxH)</td><td><Param name="size">&cNo Size Provided&r</Param></td></tr>
      
      <tr>
        <td>Power</td>
        <td>
          <Switch test="power">
            <Case value="any">Any Hatches allowed, includes Multi-Amp and Laser Hatches</Case>
            <Case value="unlockable">Regular, but upgrading tier can unlock restrictions</Case>
            <Case value="none">None</Case>
            <Case value="under4a">Lower than 4A</Case>
            <Case value="varies">Varies</Case>
            <Default>Regular</Default>
          </Switch>
        </td>
      </tr>
      
      <tr>
        <td>Overclocks</td>
        <td>
          <Switch test="oc">
            <Case value="perfect">Perfect</Case>
            <Case value="unique">Unique</Case>
            <Case value="none">None</Case>
            <Case value="mixed">Mixed</Case>
            <Case value="varies">Varies</Case>
            <Default>Imperfect</Default>
          </Switch>
        </td>
      </tr>
      
      <tr>
        <td>Maintenance</td>
        <td>
          <Switch test="reqMaintenance">
            <Case value="">Need Maintenance</Case>
            <Default>No Maintenance Needed</Default>
          </Switch>
        </td>
      </tr>
      
      <tr>
        <td>Pollution</td>
        <td>
          <If test="pollution">
            Produces &r<Param name="pollution" />&r gibbl/s pollution
            <Switch test="reqMuffler">
              <Case value="">, and require Muffler Hatch</Case>
              <Default></Default>
            </Switch>
            <Else>Produces no pollution</Else>
          </If>
        </td>
      </tr>
    </tbody>
  </table>
</IncludeOnly>